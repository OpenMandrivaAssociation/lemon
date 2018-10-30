Summary:	The Lemon Parser Generator
Name:		lemon
Version:	3.7.9
Release:	10
License:	Public Domain
Group:		Development/Other
Url:		http://www.sqlite.org/
# taken from http://www.sqlite.org/sqlite-src-3070900.zip
Source0:	http://www.sqlite.org/cvstrac/getfile/sqlite/tool/lemon.c
Source1:	http://www.sqlite.org/cvstrac/getfile/sqlite/tool/lempar.c
Source2:	lemon.rpmlintrc
Patch0:		lemon-3.7.6.2-system-template.diff

%description
Lemon is an LALR(1) parser generator for C or C++. It does the same job as
bison and yacc. But lemon is not another bison or yacc clone. It uses a
different grammar syntax which is designed to reduce the number of coding
errors. Lemon also uses a more sophisticated parsing engine that is faster than
yacc and bison and which is both reentrant and thread-safe. Furthermore, Lemon
implements features that can be used to eliminate resource leaks, making is
suitable for use in long-running programs such as graphical user interfaces or
embedded controllers.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .
%patch0 -p0

%build
%{__cc} %{optflags} -o lemon lemon.c

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/lemon

install -m0755 lemon %{buildroot}%{_bindir}/
install -m0644 lempar.c %{buildroot}%{_datadir}/lemon/lempar.c

%files
%{_bindir}/lemon
%dir %{_datadir}/lemon
%{_datadir}/lemon/lempar.c

