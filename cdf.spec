Summary:	cdf means "colorized df"
Summary(pl):	cdf to "kolorowy df"
Name:		cdf
Version:	0.1
Release:	1
License:	GPL v2+
Group:		Utilities
Source0:	http://bmp-plugins.berlios.de/misc/cdf/%{name}-%{version}.tar.gz
# Source0-md5:	8591e101a9da0844c010804445091545
URL:		http://bmp-plugins.berlios.de/misc/cdf/cdf.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cdf means "colorized df". The main features of cdf are:
- customazable color schemes
- eye-friendly capacity bars
- most of such utils needs some 3rd party libraries, python
  interpreter and so on, while cdf written in pure C

%description -l pl
cdf oznacza "kolorowy df". G³ównymi cechami cdf s±:
- schematy kolorów
- przyjemne dla oka paski zape³nienia dysków
- cdf jest napisany w czystym C, dziêki czemu nie wymaga ¿adnych
  dodatkowych bibliotek

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
