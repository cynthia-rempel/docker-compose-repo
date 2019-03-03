FROM base-terragear:build

ENV container=docker 

RUN wget \
https://download.fedoraproject.org/pub/fedora/linux/releases/28/Everything/source/tree/Packages/f/FlightGear-2017.3.1-6.fc28.src.rpm \
    && cd /tmp/ \
    && rpm2cpio /FlightGear-2017.3.1-6.fc28.src.rpm | cpio -idmv \
    && yum-builddep -y FlightGear.spec \
    && rpmbuild --rebuild --nodeps -bi /FlightGear-2017.3.1-6.fc28.src.rpm

CMD ["init"]
