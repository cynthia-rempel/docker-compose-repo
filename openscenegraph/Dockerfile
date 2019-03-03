FROM base-terragear:build

ENV container=docker 

RUN useradd osg \
    && wget \
https://download.fedoraproject.org/pub/fedora/linux/releases/28/Everything/source/tree/Packages/o/OpenSceneGraph-3.4.1-5.fc28.src.rpm \
    && cp /*.rpm /home/osg \
    && cd tmp/ \
    && rpm2cpio /OpenSceneGraph-3.4.1-5.fc28.src.rpm | cpio -idmv \
    && yum-builddep -y OpenSceneGraph.spec \
    && cp /*.rpm /home/osg \
    && cp OpenSceneGraph.spec /home/osg
COPY put-in-repo.sh /home/osg

COPY ssh/ /home/osg/.ssh

RUN chmod +x /home/osg/put-in-repo.sh \
    && mkdir -p /home/osg/rpmbuild/SOURCES/ \
    && cd /home/osg/rpmbuild/SOURCES/ \
    && rpm2cpio /OpenSceneGraph-3.4.1-5.fc28.src.rpm | cpio -idmv \
    && chown -R osg:osg /home/osg/

USER osg

WORKDIR /home/osg

RUN rpmdev-setuptree \
    && mkdir tmp \
    && cd tmp \
    && sed s'/DOCUMENTATION\=ON/DOCUMENTATION\=ON\ DYNAMIC\_OPENSCENEGRAPH\=ON/' -i ../OpenSceneGraph.spec \
    && rpmbuild --noclean --nodeps -bb ../OpenSceneGraph.spec
CMD ["/home/osg/put-in-repo.sh"]
