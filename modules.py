import pandas as pd


def descriptive_statistics(df: pd.DataFrame, name: str, axis_type: str):
    """Función para obtener estadísticas descriptivas de una fila o columna específica


    Args:
        df (pd.DataFrame): Dataframe conteniendo UK_foods
        name (str): Nombre de la columa o fila del que se desea obtener la estadística descriptiva
        axis_type (str): "column" or "row"

    Returns:
        _type_: Estadística descriptiva
    """

    if axis_type == 'column':
        if name in df.columns:
            return df[name].describe()
        else:
            return f"La columna {name} no existe en el DataFrame."
    
    elif axis_type == 'row':
        if name in df['Product'].values:
            return df[df['Product'] == name].drop('Product', axis=1).describe().loc[['mean', 'std', 'min', '25%', '50%', '75%', 'max'], :]
        else:
            return f"La fila {name} no existe en el DataFrame."
    else:
        return "El parámetro axis_type debe ser 'row' o 'column'."