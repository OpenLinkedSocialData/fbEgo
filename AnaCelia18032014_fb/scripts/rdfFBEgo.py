import social as S, percolation as P, os
import  importlib
importlib.reload(P.rdf)
importlib.reload(S.fb)
importlib.reload(S.fb.gdf2rdf)
importlib.reload(S.fb.gdf2rdf)
c=P.utils.check
fnames_=[
        ("RenatoFabbri19112014.gdf",None,"781909429","renato.fabbri"),
        ("PedroPauloRocha10032013.gdf",None,"836944624","dpedropaulorocha"),
        ("AnaCelia18032014.gdf",None,"1450596979",0),
        ("FabiBorges08032014.gdf",None,"598339469","antennarush"),
        ("Poppi18032014.gdf",None,"100000099352333","ricardopoppi"),
        ("ElenaGarnelo04032014.gdf",None,"1361932044","elena.garnelo"),
        ("GeorgeSanders08032014.gdf",None,"1347483608","george.sander"),
        ("GraziMachado18032014.gdf",None,"1847090892","GrazielleMachado"),
        ("RenatoFabbri19032014.gdf",None,"781909429","renato.fabbri")
        ]
fpath="./publishing/fb3/"
#dpath="../data/fb/gdf/ego/"
dpath="../data/fb/gdf/posAvlab/"
umbrella_dir="fbEgo/"
scriptpath=os.path.realpath(__file__)
for fnames in fnames_[2:]:
    S.fb.triplifyGDF(dpath=dpath,
                     fname=fnames[0],
                     fnamei=None,
                     fpath=fpath,
                     scriptpath=scriptpath,
                     uid=fnames[2],
                     sid=fnames[3],
                     fb_link=None,
                     ego=True,
                     umbrella_dir=umbrella_dir)

