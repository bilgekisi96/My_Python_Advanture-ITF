
"""
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
def domain_name(domain):
    points,com=[i for i in range(len(domain)) if domain[i]=="." or domain[i]=="/"],".com"
    index=domain.index(com)
    crack_dom=domain[points[1]+1:index]
    if crack_dom[3]==".":return print(crack_dom[4:])
    else:return print(crack_dom)
domain_name("https://www.cnet.com")
domain_name("http://www.zombie-bites.com")
domain_name("http://github.com/carbonfive/raygun")



def domain_name(url):
    return print(url.split("//")[-1].split("www.")[-1].split(".")[0])
domain_name("http://github.com/carbonfive/raygun")