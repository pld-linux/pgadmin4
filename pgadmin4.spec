# TODO:
# - install py stuff
Summary:	Powerful administration and development platform for the PostgreSQL
Summary(pl.UTF-8):	Potężna platforma do administrowania i programowania bazy PostgreSQL
Name:		pgadmin4
Version:	3.3
Release:	0.1
License:	Artistic
Group:		Applications/Databases
Source0:	http://ftp.postgresql.org/pub/pgadmin/pgadmin4/v%{version}/source/%{name}-%{version}.tar.gz
# Source0-md5:	6dfd363dd2cf21efe35330c6e4a87f03
Source1:	%{name}.desktop
URL:		http://pgadmin3.org/
BuildRequires:	python3-devel
BuildRequires:	postgresql-backend-devel >= 8.3.0
BuildRequires:	postgresql-devel >= 8.3.0
BuildRequires:	qt5-qmake
BuildRequires: Qt5Core-devel
BuildRequires: Qt5Gui-devel
BuildRequires: Qt5Network-devel
BuildRequires: Qt5Widgets-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pgAdmin III is designed to answer the needs of all users, from writing
simple SQL queries to developing complex databases. The graphical
interface supports all PostgreSQL features and makes administration
easy. The application also includes a query builder, an SQL editor, a
server-side code editor and much more. pgAdmin III is released with an
installer and does not require any additional driver to communicate
with the database server.

%description -l pl.UTF-8
pgAdmin III został zaprojektowany jako odpowiedź na potrzeby
wszystkich użytkowników, od pisania prostych zapytań SQL do tworzenia
skomplikowanych baz danych. Graficzny interfejs obsługuje wszystkie
możliwości PostgreSQL-a i ułatwia administrowanie. Aplikacja zawiera
także narzędzie do budowania zapytań, edytor SQL, edytor kodu po
stronie serwera i wiele więcej. pgAdmin III został wydany z
instalatorem i nie wymaga żadnego dodatkowego sterownika do
komunikowania z serwerem baz danych.

%prep
%setup -q

%build
cd runtime

PYTHON_CONFIG=%{_bindir}/python3-config \
qmake-qt5
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} -C runtime install \
	DESTDIR=$RPM_BUILD_ROOT

install runtime/pgAdmin4 $RPM_BUILD_ROOT%{_bindir}/pgadmin4

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p runtime/pgAdmin4.png $RPM_BUILD_ROOT%{_pixmapsdir}/pgadmin4.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README docs/en_US
%attr(755,root,root) %{_bindir}/pgadmin4
%{_desktopdir}/pgadmin4.desktop
%{_pixmapsdir}/pgadmin4.png
