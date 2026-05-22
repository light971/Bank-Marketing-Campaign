import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    """Charge le dataset brut Bank Marketing."""
    df = pd.read_csv(path, sep=";")
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoyage et typage des colonnes."""
    df = df.copy()
    # Renommage pour lisibilité
    df.rename(columns={"y": "subscribed"}, inplace=True)
    # Encodage cible
    df["subscribed_bin"] = (df["subscribed"] == "yes").astype(int)
    # Remplacement des "unknown" par NaN
    df.replace("unknown", pd.NA, inplace=True)
    # Typage
    df["age"] = df["age"].astype(int)
    return df

def save_processed(df: pd.DataFrame, path: str) -> None:
    """Sauvegarde les données nettoyées."""
    df.to_csv(path, index=False)
    print(f"✅ Données sauvegardées : {path}")