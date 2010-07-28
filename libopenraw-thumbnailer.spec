Summary:	RawThumbnailer - RAW files thumbnailer for the GNOME Nautilus file manager
Summary(pl.UTF-8):	RawThumbnailer - program do miniaturek plików RAW dla zarządcy plików Nautilus
Name:		libopenraw-thumbnailer
Version:	0.99.1
Release:	0.1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://libopenraw.freedesktop.org/download/raw-thumbnailer-%{version}.tar.gz
# Source0-md5:	8b166320b17fa906bf0503ed3b6ba226
URL:		http://libopenraw.freedesktop.org/wiki/RawThumbnailer
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libgsf-gnome-devel
BuildRequires:	libopenraw-gnome-devel >= 0.0.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RawThumbnailer is a thumbnailer for RAW files that works with the
GNOME Nautilus file manager.

%description -l pl.UTF-8
RawThumbnailer to program generujący miniaturki plików RAW działający
z zarządcą plików Nautilus ze środowiska GNOME.

%prep
%setup -q -n raw-thumbnailer-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install raw-thumbnailer.schemas
%update_mime_database

%preun
%gconf_schema_uninstall raw-thumbnailer.schemas

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/raw-thumbnailer
%{_datadir}/mime/packages/raw-thumbnailer.xml
%{_sysconfdir}/gconf/schemas/raw-thumbnailer.schemas
