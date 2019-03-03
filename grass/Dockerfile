# https://blog.packagecloud.io/eng/2015/05/11/building-rpm-packages-with-mock/
FROM base-terragear:build

ENV container=docker 

RUN useradd grass

COPY put-in-repo.sh /home/grass

COPY ssh/ /home/grass/.ssh

RUN chmod +x /home/grass/put-in-repo.sh \
    && chown -R grass:grass /home/grass/
    
USER grass

WORKDIR /home/grass

RUN rpmdev-setuptree \
    && wget \
https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/g/grass-7.6.0-3.fc30.src.rpm \
    && mkdir tmp \
    && cd tmp \
    && mock -r epel-7-x86_64 rpmbuild --rebuild -bi ../grass-7.6.0-3.fc30.src.rpm

CMD ["/home/grass/put-in-repo.sh"]
