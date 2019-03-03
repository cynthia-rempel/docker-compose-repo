FROM base-terragear:build

ENV container=docker 

# generate dependencies by running openscenegraph project and docker copy the rpms
COPY dependencies /dependencies

RUN yum -y localinstall /dependencies \
    && wget \
https://download.fedoraproject.org/pub/fedora/linux/releases/28/Everything/source/tree/Packages/s/SimGear-2017.3.1-3.fc28.src.rpm \
    && cd tmp/ \
    && rpm2cpio /SimGear-2017.3.1-3.fc28.src.rpm | cpio -idmv \
    && yum-builddep -y SimGear.spec
    && rm -f /usr/bin/cmake \
    && ln -s /usr/bin/cmake3 /usr/bin/cmake \
    && cd /tmp \
    && rpmbuild --rebuild --nodeps -bi /SimGear-2017.3.1-3.fc28.src.rpm

CMD ["init"]
