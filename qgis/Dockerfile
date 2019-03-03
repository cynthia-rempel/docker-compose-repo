# https://blog.packagecloud.io/eng/2015/05/11/building-rpm-packages-with-mock/
FROM base-terragear:build

ENV container=docker 

RUN useradd qgis

COPY put-in-repo.sh /home/qgis

COPY ssh/ /home/qgis/.ssh

RUN chmod +x /home/qgis/put-in-repo.sh \
    && chown -R qgis:qgis /home/qgis/
    
USER qgis

WORKDIR /home/qgis
# QGIS Server
# QGIS Web Client
RUN rpmdev-setuptree \
    && wget \
       https://download.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/source/tree/Packages/q/qgis-3.4.4-3.fc30.src.rpm \
    && mkdir tmp \
    && cd tmp \
    && mock -r epel-7-x86_64 rpmbuild --rebuild -bi ../qgis-3.4.4-3.fc30.src.rpm

CMD ["/home/qgis/put-in-repo.sh"]
