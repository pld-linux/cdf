Summary:	cdf - "colorized df"
Summary(pl.UTF-8):   cdf - "kolorowy df"
Name:		cdf
Version:	0.2
Release:	1
License:	GPL v2+
Group:		Utilities
Source0:	http://download.berlios.de/bmp-plugins/%{name}-%{version}.tar.gz
# Source0-md5:	1afd130f6c562700e8ad05724c6e1a9d
URL:		http://bmp-plugins.berlios.de/misc/cdf/cdf.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cdf means "colorized df". The main features of cdf are:
- customazable color schemes
- eye-friendly capacity bars
- most of such utils needs some 3rd party libraries, python
  interpreter and so on, while cdf written in pure C

%description -l pl.UTF-8
cdf oznacza "kolorowy df". Głównymi cechami cdf są:
- schematy kolorów
- przyjemne dla oka paski zapełnienia dysków
- cdf jest napisany w czystym C, dzięki czemu nie wymaga żadnych
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
