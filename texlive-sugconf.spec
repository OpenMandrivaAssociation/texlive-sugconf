Name:		texlive-sugconf
Version:	58752
Release:	2
Summary:	SAS(R) user group conference proceedings document class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conferences/sugconf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sugconf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sugconf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class may be used to typeset articles to be published in
the proceedings of SAS(R) User group conferences and workshops.
The layout produced by the class is based on that published by
SAS Institute (2006).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sugconf
%doc %{_texmfdistdir}/doc/latex/sugconf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
