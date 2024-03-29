%define         _name sofk

Summary:	KDE style - %{_name}
Summary(pl.UTF-8):	Styl do KDE - %{_name}
Name:		kde-style-%{_name}
Version:	0.0.3
Release:	1
License:	X11
Group:		Themes
Source0:	http://www.kde-look.org/content/files/44656-sofk.style-%{version}.tar.bz2
# Source0-md5:	dda8f89e811b8c3274af3552d8cde6f5
URL:		http://www.kde-look.org/content/show.php?content=44656
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a Serenity based, smooth, light KDE theme.

%description -l pl.UTF-8
%{_name} to gładki i lekki styl dla KDE bazujący na temacie Serenity.

%prep
%setup -q -n %{_name}.style-%{version}

%build
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/plugins/styles/*.la
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_datadir}/apps/kstyle/themes/*.themerc
