#!/bin/bash
ssh repo.rpm mkdir -p /var/www/html/repos/graphics/Packages
scp rpmbuild/RPMS/x86_64/* repo.rpm:/var/www/html/repos/graphics/Packages/
ssh repo.rpm createrepo --update /var/www/html/repos/
