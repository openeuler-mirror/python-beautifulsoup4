Name:           python-beautifulsoup4
Version:        4.6.3
Release:        3
Summary:        HTML/XML parser for quick-turnaround projects
License:        MIT
URL:            http://www.crummy.com/software/BeautifulSoup/
Source0:        https://files.pythonhosted.org/packages/source/b/beautifulsoup4/beautifulsoup4-%{version}.tar.gz
Patch0:         fixed-the-definition-of-the-default-XML-namespace-with-lxml-4.4.patch

BuildArch:      noarch
BuildRequires:  python2-devel >= 2.7 python2-html5lib python2-setuptools python2-lxml python2-tools
BuildRequires:  python3-devel python3-html5lib python3-setuptools python3-lxml

%global _description\
This package provides a python library which is designed for quick\
turnaround projects.It provides methods for navigating and modifying\
a parse tree.It can help convert incoming documents to Unicode\
and outgoing documents to utf-8.

%description %_description

%package     -n python2-beautifulsoup4
Summary:        %summary
%description -n python2-beautifulsoup4 %_description
Requires:       python2-lxml
%{?python_provide:%python_provide python2-beautifulsoup4}

%package     -n python3-beautifulsoup4
Summary:        %summary
%description -n python3-beautifulsoup4 %_description
Obsoletes:      python3-BeautifulSoup < 1:3.2.1-2
Requires:       python3-lxml

%prep
%setup -q -n beautifulsoup4-%{version}
%autopatch -p1
mv AUTHORS.txt AUTHORS.txt.iso
iconv -f ISO-8859-1 -t UTF-8 -o AUTHORS.txt AUTHORS.txt.iso
touch -r AUTHORS.txt.iso AUTHORS.txt
rm -rf %{py3dir} 
cp -a . %{py3dir}

%build
%{py2_build}
pushd %{py3dir}
2to3 --write --nobackups .
%{py3_build}

%install
%{py2_install}
pushd %{py3dir}
%{py3_install}

%check
#%{__python2} -m unittest discover -s bs4
pushd %{py3dir}
%{__python3} -m unittest discover -s bs4


%files -n python2-beautifulsoup4
%{python2_sitelib}/bs4
%{python2_sitelib}/beautifulsoup4-%{version}*.egg-info
%doc TODO.txt AUTHORS.txt NEWS.txt
%license COPYING.txt

%files -n python3-beautifulsoup4
%{python3_sitelib}/bs4
%{python3_sitelib}/beautifulsoup4-%{version}*.egg-info
%doc TODO.txt AUTHORS.txt NEWS.txt
%license COPYING.txt

%changelog
* Mon May 24 2020 yangfeiyu <yangfeiyu2@huawei.com> - 4.6.3-3
- fixed the definition of the default XML namespace with lxml 4.4

* Sat Sep 21 2019 yangfeiyu <yangfeiyu2@huawei.com> - 4.6.3-2
- spec init
