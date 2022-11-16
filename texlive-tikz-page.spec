Name:		texlive-tikz-page
Version:	42039
Release:	1
Summary:	Small macro to help building nice and complex layout materials
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-page
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-page.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-page.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-page.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a small macro to help building nice and
complex layout materials.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tikz-page
%{_texmfdistdir}/tex/latex/tikz-page
%doc %{_texmfdistdir}/doc/latex/tikz-page

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
