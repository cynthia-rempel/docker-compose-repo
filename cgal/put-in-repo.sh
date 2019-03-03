#!/bin/bash
ssh repo.rpm mkdir -p /var/www/html/repos/math/Packages
scp rpmbuild/RPMS/x86_64/CGAL-* repo.rpm:/var/www/html/repos/math/Packages/
ssh repo.rpm createrepo --update /var/www/html/repos/
