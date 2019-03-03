FROM base-terragear:build

ENV container=docker 

# COPY gdal.spec
# https://download.fedoraproject.org/pub/epel/7/SRPMS/Packages/g/gdal-1.11.4-3.el7.src.rpm \
#    && mkdir /gdal-2.2.4 \
#    && cd gdal-2.2.4/ \
#     && rpm2cpio /gdal-1.11.4-3.el7.src.rpm | cpio -idmv \
# Even more inconsistent dependency craziness... use old spec file, and new tarball
# RUN yum -y install texlive-epstopdf texlive-latex-bin-bin texlive-collection-fontsrecommended lyx-fonts centos-release-scl-rh \
#    && yum -y install rh-java-common-javapackages-local rh-java-common-python-javapackages \
#    && cp -r /opt/rh/rh-java-common/root/lib/python2.7/site-packages/javapackages/{cache,common,ivy,maven,metadata} /usr/lib/python2.7/site-packages/javapackages/ \ 
COPY gdal.spec /

RUN wget \
https://download.fedoraproject.org/pub/fedora/linux/releases/28/Everything/source/tree/Packages/g/gdal-2.2.4-2.fc28.src.rpm \
    && cd  /root/rpmbuild/SOURCES/ \
    && rpm2cpio /gdal-2.2.4-2.fc28.src.rpm | cpio -idmv \
    && cd /tmp \
    && rpm2cpio /gdal-2.2.4-2.fc28.src.rpm | cpio -idmv \
    && yum-builddep -y /gdal.spec
    && yum -y install texlive-latex-bin \
           texlive-metafont-bin \
           texlive-cm \
           texlive-collection-htmlxml \
           texlive-xtab \
           texlive-multirow \
           texlive-ec \
           texlive-sectsty \
           texlive-tocloft \
           texlive-epstopdf-bin

RUN rpmbuild --noclean --nodeps -bb /gdal.spec
RUN useradd gdal.rpm
COPY ssh/ /root
CMD ["init"]
