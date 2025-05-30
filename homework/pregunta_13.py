def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    import pandas as pd

    tbl0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    df_merged = pd.merge(tbl0, tbl2, on="c0")
    df_result = df_merged.groupby("c1")["c5b"].sum()

    return df_result
