FROM base-terragear:build

ENV container=docker 

RUN useradd gazebo \
    && wget \
https://download.fedoraproject.org/pub/fedora/linux/releases/28/Everything/source/tree/Packages/g/gazebo-8.3.0-1.fc28.src.rpm \
    && cd tmp \
    && rpm2cpio /gazebo-8.3.0-1.fc28.src.rpm | cpio -idmv \
    && yum-builddep -y CGAL.spec \
    && rm -f /usr/bin/cmake \
    && ln -s /usr/bin/cmake3 /usr/bin/cmake \
    && cp /*.rpm /home/gazebo

COPY put-in-repo.sh /home/gazebo

COPY ssh/ /home/gazebo/.ssh

RUN chmod +x /home/gazebo/put-in-repo.sh \
    && chown -R gazebo:gazebo /home/gazebo/
    
USER gazebo

WORKDIR /home/gazebo

RUN rpmdev-setuptree \
    && mkdir tmp \
    && cd tmp \
    && rpmbuild --rebuild --nodeps -bi ../gazebo-8.3.0-1.fc28.src.rpm

CMD ["/home/cgal/put-in-repo.sh"]
