Summary:	The Lemon Parser Generator
Name:		lemon
Version:	3.7.4
Release:	%mkrel 1
License:	Public Domain
Group:		Development/Other
URL:		http://www.sqlite.org/
Source0:	http://www.sqlite.org/cvstrac/getfile/sqlite/tool/lemon.c
Source1:	http://www.sqlite.org/cvstrac/getfile/sqlite/tool/lempar.c
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%build

gcc %{optflags} -o lemon lemon.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 lemon %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc lempar.c
%{_bindir}/lemon

