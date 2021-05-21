#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-LWP-MediaTypes
Version  : 6.04
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-MediaTypes-6.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/LWP-MediaTypes-6.04.tar.gz
Summary  : 'guess media type for a file or a URL'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-LWP-MediaTypes-license = %{version}-%{release}
Requires: perl-LWP-MediaTypes-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
NAME
LWP::MediaTypes - guess media type for a file or a URL
SYNOPSIS
use LWP::MediaTypes qw(guess_media_type);
$type = guess_media_type("/tmp/foo.gif");

%package dev
Summary: dev components for the perl-LWP-MediaTypes package.
Group: Development
Provides: perl-LWP-MediaTypes-devel = %{version}-%{release}
Requires: perl-LWP-MediaTypes = %{version}-%{release}

%description dev
dev components for the perl-LWP-MediaTypes package.


%package license
Summary: license components for the perl-LWP-MediaTypes package.
Group: Default

%description license
license components for the perl-LWP-MediaTypes package.


%package perl
Summary: perl components for the perl-LWP-MediaTypes package.
Group: Default
Requires: perl-LWP-MediaTypes = %{version}-%{release}

%description perl
perl components for the perl-LWP-MediaTypes package.


%prep
%setup -q -n LWP-MediaTypes-6.04
cd %{_builddir}/LWP-MediaTypes-6.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-LWP-MediaTypes
cp %{_builddir}/LWP-MediaTypes-6.04/LICENSE %{buildroot}/usr/share/package-licenses/perl-LWP-MediaTypes/e9330dd55cc5b12a4e89bca611863182e2acf7d1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/LWP::MediaTypes.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-LWP-MediaTypes/e9330dd55cc5b12a4e89bca611863182e2acf7d1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/LWP/MediaTypes.pm
/usr/lib/perl5/vendor_perl/5.34.0/LWP/media.types
