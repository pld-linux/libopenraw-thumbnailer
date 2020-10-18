Summary:	RawThumbnailer - RAW files thumbnailer for the GNOME Nautilus file manager
Summary(pl.UTF-8):	RawThumbnailer - program do miniaturek plików RAW dla zarządcy plików Nautilus
Name:		libopenraw-thumbnailer
Version:	3.0.0
Release:	4
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://libopenraw.freedesktop.org/download/raw-thumbnailer-%{version}.tar.bz2
# Source0-md5:	fc56f327b3e2b2c647abd99b728b27a2
Patch0:		%{name}-libopenraw.patch
URL:		https://libopenraw.freedesktop.org/wiki/RawThumbnailer
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libopenraw-gnome-devel >= 0.0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	shared-mime-info
Requires:	libopenraw-gnome >= 0.0.9
Obsoletes:	raw-thumbnailer < 0.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RawThumbnailer is a thumbnailer for RAW files that works with the
GNOME Nautilus file manager.

%description -l pl.UTF-8
RawThumbnailer to program generujący miniaturki plików RAW działający
z zarządcą plików Nautilus ze środowiska GNOME.

%prep
%setup -q -n raw-thumbnailer-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/raw-thumbnailer
%{_datadir}/mime/packages/raw-thumbnailer.xml
%{_datadir}/thumbnailers/raw.thumbnailer
