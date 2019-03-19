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
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
    && yum -y install \
           epel-release \
           centos-release-scl \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \
    && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-SCLo \ 
    && yum -y install \
           bzip2 \
           cmake3 \
           gcc-c++ \
           java-1.8.0-openjdk-devel \
           make \
           mock \
           openssh-clients \
           zip \
           rpm-build \
           rpmdevtools \
           wget \
           yum-utils \
    && rm -rf /usr/share/java \
    && ln -s /opt/rh/rh-maven35/root/usr/share/java /usr/share \
    && useradd nexus \
    && mkdir -p /home/nexus/rpmbuild/SOURCES \
    && cd /home/nexus/rpmbuild/SOURCES \
    && wget https://github.com/sonatype/nexus-public/archive/release-3.15.2-01.tar.gz

COPY files/nexus.spec /home/nexus/
RUN  yum-builddep -y /home/nexus/nexus.spec \
    && chown -R nexus:nexus /home/nexus/
USER nexus
RUN mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} \
    && echo '%_topdir %(echo $HOME)/rpmbuild' > ~/.rpmmacros \
    && rpmbuild --noclean --nodeps -bb /home/nexus/nexus.spec
CMD ["init"]
