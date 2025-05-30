def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a` y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.
    """
    import pandas as pd
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    df = df.sort_values(by=["c0", "c5a"])  # 👈 ordenar por clave antes de unir
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)
    df = df.groupby("c0")["c5"].apply(lambda x: ",".join(x)).reset_index()
    return df
