FROM base-terragear:build

ENV container=docker 

RUN useradd cgal \
    && wget \
http://mirror.math.princeton.edu/pub/fedora/linux/releases/28/Everything/source/tree/Packages/c/CGAL-4.11.1-1.fc28.src.rpm \
    && cd tmp \
    && rpm2cpio /CGAL-4.11.1-1.fc28.src.rpm | cpio -idmv \
    && yum-builddep -y CGAL.spec \
    && rm -f /usr/bin/cmake \
    && ln -s /usr/bin/cmake3 /usr/bin/cmake \
    && cp /*.rpm /home/cgal

COPY put-in-repo.sh /home/cgal

COPY ssh/ /home/cgal/.ssh

RUN chmod +x /home/cgal/put-in-repo.sh \
    && chown -R cgal:cgal /home/cgal/
    
USER cgal

WORKDIR /home/cgal

RUN rpmdev-setuptree \
    && wget \
http://mirror.math.princeton.edu/pub/fedora/linux/releases/28/Everything/source/tree/Packages/c/CGAL-4.11.1-1.fc28.src.rpm \
    && mkdir tmp \
    && cd tmp \
    && rpmbuild --rebuild --nodeps -bi ../CGAL-4.11.1-1.fc28.src.rpm 
# rpmbuild --noclean --nodeps -bb 
CMD ["/home/cgal/put-in-repo.sh"]
