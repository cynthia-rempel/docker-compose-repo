FROM base-terragear:build

ENV container=docker 

COPY spec/* /
RUN useradd fast-cdr \
    && mkdir -p /home/fast-cdr/rpmbuild/SOURCES/ \
    && yum-builddep -y /FAST-CDR.spec \
    && cp FAST-CDR.spec /home/fast-cdr \
    && cp fastcdr-1.0.6-endian.patch /home/fast-cdr/rpmbuild/SOURCES/ \
    && rm -f /usr/bin/cmake \
    && ln -s /usr/bin/cmake3 /usr/bin/cmake

COPY put-in-repo.sh /home/fast-cdr

# to generate the keys, run make-keys.sh
COPY ssh/ /home/fast-cdr/.ssh

RUN chmod +x /home/fast-cdr/put-in-repo.sh \
    && chown -R fast-cdr:fast-cdr /home/fast-cdr/

USER fast-cdr

WORKDIR /home/fast-cdr

RUN rpmdev-setuptree \
    && cd /home/fast-cdr/rpmbuild/SOURCES/ \
    && wget https://github.com/eProsima/Fast-CDR/archive/v1.0.8.tar.gz \
    && mkdir /home/fast-cdr/tmp \
    && cd /home/fast-cdr/tmp \
    && rpmbuild --noclean --nodeps -bb ../FAST-CDR.spec

CMD ["/home/fast-cdr/put-in-repo.sh"]
