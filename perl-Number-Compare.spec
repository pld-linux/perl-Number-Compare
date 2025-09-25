#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Number
%define		pnam	Compare
Summary:	Number::Compare - numeric comparisons
Summary(pl.UTF-8):	Number::Compare - porównywanie liczb
Name:		perl-Number-Compare
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Number/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ded4085a8fc96328742785574ca65208
URL:		https://metacpan.org/dist/Number-Compare
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number::Compare compiles a simple comparison to an anonymous
subroutine, which you can call with a value to be tested again.

%description -l pl.UTF-8
Number::Compare kompiluje proste porównanie do anonimowej biblioteki,
którą można wywołać ponownie dla porównywanej wartości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Number/Compare.pm
%{_mandir}/man3/*
