# Build nexus.zip from source, because it's good to have control
# Due to log-running nature of build, heavilty leverages image-caching
# End result is a zip file, which would then be installed on a fresh
# production container
# TODO: add the env variables for JAVA, MAVEN 
# TODO: summarize in README
#       https://www.usenix.org/conference/ures14west/summit-program/presentation/mckern
# TODO: use docker diff on each step to determine what changes each command in nexus guide does
FROM registry.hub.docker.com/library/centos:centos7

ENV container=docker

# install the build tools
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    && yum -y update \
    && yum -y install epel-release -y \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \
    && yum -y install centos-release-scl \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo \
    && yum -y install createrepo \
                      curl \
                      git \
                      java-1.8.0-openjdk \
                      java-1.8.0-openjdk-devel \
                      rh-maven35 \
                      rh-maven35-ant \
                      rh-maven35-ivy \
                      rh-maven35-jansi \
                      rh-maven35-jdependency \
                      rh-maven35-jline \
                      rh-maven35-maven-model \
                      rh-maven35-maven-plugin-plugin \
                      rh-maven35-maven-lib \
                      rh-maven35-maven-shade-plugin \
                      rh-maven35-maven-settings \
                      rh-maven35-plexus-containers-container-default \
                      rh-maven35-xmvn-connector-aether \
                      tar \
                      wget \
                      which \
    && yum clean all \
    && rm -rf /usr/share/java \
    && ln -s /opt/rh/rh-maven35/root/usr/share/java /usr/share

RUN yum -y install bzip2 \
    && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && tar -xf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/ \
    && rm -rf phantomjs-2.1.1-linux-x86_64 \
    && git clone https://github.com/sonatype/nexus-public.git \
    && cd nexus-public \
    && git checkout -b jacoco_tests

# now that the project is cloned cd into it
WORKDIR /nexus-public

# replace elastic-search dependency with elastic-search on main maven site to
# stop an error
COPY 0001-fix-elastic-search-dependency.patch /

# Pre-stage pom.xml's to better enable parallel building
RUN git apply /0001-fix-elastic-search-dependency.patch \
    && mkdir -p /root/repository/org/sonatype/nexus/nexus-components/3.16.0-SNAPSHOT/ \
    && cp components/pom.xml /root/repository/org/sonatype/nexus/nexus-components/3.16.0-SNAPSHOT/nexus-components-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/nexus-parent/3.16.0-SNAPSHOT \
    && cp pom.xml /root/repository/org/sonatype/nexus/nexus-parent/3.16.0-SNAPSHOT/nexus-parent-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/nexus-thirdparty-bundles/3.16.0-SNAPSHOT \
    && cp thirdparty-bundles/pom.xml /root/repository/org/sonatype/nexus/nexus-thirdparty-bundles/3.16.0-SNAPSHOT/nexus-thirdparty-bundles-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/nexus-assemblies/3.16.0-SNAPSHOT \
    && cp assemblies/pom.xml /root/repository/org/sonatype/nexus/nexus-assemblies/3.16.0-SNAPSHOT/nexus-assemblies-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/nexus-pax-logging/3.16.0-SNAPSHOT \
    && cp components/nexus-pax-logging/pom.xml /root/repository/org/sonatype/nexus/nexus-pax-logging/3.16.0-SNAPSHOT/nexus-pax-logging-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/nexus-task-logging/3.16.0-SNAPSHOT/ \
    && cp components/nexus-task-logging/pom.xml /root/repository/org/sonatype/nexus/nexus-task-logging/3.16.0-SNAPSHOT/nexus-task-logging-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/buildsupport/nexus-buildsupport-all/3.16.0-SNAPSHOT/ \
    && cp buildsupport/all/pom.xml /root/repository/org/sonatype/nexus/buildsupport/nexus-buildsupport-all/3.16.0-SNAPSHOT/nexus-buildsupport-all-3.16.0-SNAPSHOT.pom \
    && mkdir -p /root/repository/org/sonatype/nexus/buildsupport/nexus-buildsupport/3.16.0-SNAPSHOT/ \
    && cp buildsupport/pom.xml /root/repository/org/sonatype/nexus/buildsupport/nexus-buildsupport/3.16.0-SNAPSHOT/nexus-buildsupport-3.16.0-SNAPSHOT.pom

# build incrementally to reduce errors related to parallelism
RUN cd buildsupport \
    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository -Dmaven.test.skip=true install

# need the nexus-repository tests jar to build the nexus-repository-maven plugin
RUN cd components \
    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository -Dmaven.test.skip=true install \
    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository -pl nexus-repository install -am

# Build the plugins
RUN cd plugins \
    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository -Dmaven.test.skip=true install

# Finally, complete the base build!
RUN /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository -Dmaven.test.skip=true install

# Make technical documentation
COPY pom.xml /nexus-public/
RUN mkdir -p /root/repository/org/sonatype/nexus/plugins/nexus-blobstore-group/3.16.0-SNAPSHOT/
COPY nexus-blobstore-group-3.16.0-SNAPSHOT.pom /root/repository/org/sonatype/nexus/plugins/nexus-blobstore-group/3.16.0-SNAPSHOT/
RUN cp pom.xml /root/repository/org/sonatype/nexus/nexus-parent/3.16.0-SNAPSHOT/nexus-parent-3.16.0-SNAPSHOT.pom \
    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository org.apache.maven.plugins:maven-site-plugin:3.7.1:site
RUN /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository org.apache.maven.plugins:maven-site-plugin:3.7.1:stage

# RUN /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install org.jacoco:jacoco-maven-plugin:report

# RUN cd components \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C clean dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install -Dmaven.test.skip=true
# RUN cd components/nexus-repository \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C clean dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install
# RUN cd components \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install
# RUN cd assemblies \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C clean dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install
# RUN cd plugins \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C clean dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install -Dmaven.test.skip=true
# RUN cd plugins/nexus-repository-npm \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install
# RUN cd plugins \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C dependency:go-offline -Dmaven.repo.local=/root/repository org.jacoco:jacoco-maven-plugin:prepare-agent install

# RUN cd /nexus-public/ \
#    && /opt/rh/rh-maven35/root/usr/bin/mvn -T 20C install dependency:go-offline -Dmaven.repo.local=/root/repository -Dtest='!ScheduledTaskEventsTest' install test
CMD [ "init" ]
