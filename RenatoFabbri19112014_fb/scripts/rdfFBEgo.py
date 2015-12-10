import social as S, percolation as P, os
import  importlib
importlib.reload(P.rdf)
importlib.reload(S.fb)
importlib.reload(S.fb.gdf2rdf)
importlib.reload(S.fb.gdf2rdf)
c=P.utils.check
fnames_=[("RenatoFabbri19112014.gdf",None,"781909429","renato.fabbri"),]
fpath="./publishing/fb3/"
dpath="../data/fb/gdf/ego/"
umbrella_dir="fbEgo/"
scriptpath=os.path.realpath(__file__)
for fnames in fnames_:
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

