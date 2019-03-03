# http://wiki.flightgear.org/TerraGear
# TODO: https://schneide.blog/2013/02/11/build-a-rpm-package-using-cmake/
FROM base-terragear:build

ENV container=docker 

# generate dependencies by running the other projects and docker copy the rpms
COPY dependencies /dependencies

# RUN yum -y localinstall /dependencies \
RUN yum -y install git \
     && wget https://getfedora.org/static/CFC659B9.txt \
     && mv CFC659B9.txt /etc/pki/rpm-gpg/RPM-GPG-KEY-FEDORA30 \
     && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-FEDORA30 \
     && git clone --single-branch --branch scenery/ws2.0 https://git.code.sf.net/p/flightgear/terragear \
     && wget https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/s/SimGear-2018.3.2-2.fc30.src.rpm \
     && cd /dependencies \
     && yum -y localinstall Open* \
     && yum -y localinstall /dependencies/CGAL-* \
     && yum -y localinstall /dependencies/gdal-libs-2.2.4-2.el7.x86_64.rpm \
     && yum -y localinstall /dependencies/gdal-devel-2.2.4-2.el7.x86_64.rpm \
     && cd /tmp \
     && rpm2cpio /SimGear-2018.3.2-2.fc30.src.rpm | cpio -idmv \
     && yum-builddep -y SimGear.spec \
     && rm -f /usr/bin/cmake \
     && ln -s /usr/bin/cmake3 /usr/bin/cmake \
     && mkdir -p /usr/include/boost/core \
     && ln -s /usr/include/boost/utility/enable_if.hpp \
              /usr/include/boost/core/enable_if.hpp \
     && cd /root/rpmbuild/SOURCES/ \
     && rpm2cpio /SimGear-2018.3.2-2.fc30.src.rpm | cpio -idmv
RUN cd /tmp \
    && sed s/.ldconfig/\#\ ldconfig/ -i /tmp/SimGear.spec \
    && rpmbuild --noclean --nodeps -bb /tmp/SimGear.spec
RUN  yum -y localinstall /root/rpmbuild/RPMS/x86_64/SimGear-*
RUN rpmbuild --noclean -bb /terragear/TerraGear.spec

CMD ["init"]
