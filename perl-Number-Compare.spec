%include	/usr/lib/rpm/macros.perl
%define	pdir	Number
%define	pnam	Compare
Summary:	Number::Compare - numeric comparisons
Summary(pl):	Number::Compare - porównywanie liczb
Name:		perl-Number-Compare
Version:	0.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number::Compare compiles a simple comparison to an anonymous
subroutine, which you can call with a value to be tested again.

%description -l pl
Number::Compare kompiluje proste porównanie do anonimowej biblioteki,
któr± mo¿na wywo³aæ ponownie dla porównywanej warto¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Number/Compare.pm
%{_mandir}/man3/*
