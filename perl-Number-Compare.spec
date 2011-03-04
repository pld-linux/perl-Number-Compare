#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Number
%define		pnam	Compare
Summary:	Number::Compare - numeric comparisons
Summary(pl.UTF-8):	Number::Compare - porównywanie liczb
Name:		perl-Number-Compare
Version:	0.01
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Number/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	519a4434e35033e9bd034d27cd2fd299
URL:		http://search.cpan.org/dist/Number-Compare/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
