import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

PALETTE = {"yes": "#1D9E75", "no": "#D85A30"}

def plot_conversion_by_category(df, col, title=None, save_path=None):
    """Taux de conversion par catégorie d'une variable."""
    rates = (df.groupby(col)["subscribed"]
                .value_counts(normalize=True)
                .unstack()
                .sort_values("yes", ascending=False))
    
    ax = rates["yes"].plot(kind="bar", color="#1D9E75", figsize=(10, 5))
    ax.set_title(title or f"Taux de conversion par {col}", fontsize=14)
    ax.set_ylabel("Taux de conversion")
    ax.set_xlabel(col)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.0%}"))
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()

def plot_distribution(df, col, hue="subscribed", save_path=None):
    """Distribution d'une variable numérique selon la conversion."""
    fig, ax = plt.subplots(figsize=(10, 5))
    for val, color in PALETTE.items():
        subset = df[df[hue] == val]
        subset[col].plot(kind="kde", ax=ax, label=val, color=color)
    ax.set_title(f"Distribution de {col} selon la souscription")
    ax.legend(title="Souscrit")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()

def plot_campaign_efficiency(df, save_path=None):
    """Taux de conversion selon le nombre de contacts campagne."""
    conv = (df.groupby("campaign")["subscribed_bin"]
                .mean()
                .reset_index()
                .rename(columns={"subscribed_bin": "conversion_rate"}))
    conv = conv[conv["campaign"] <= 15]
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(conv["campaign"], conv["conversion_rate"], color="#378ADD")
    ax.set_title("Efficacité de la campagne selon le nb de contacts")
    ax.set_xlabel("Nombre de contacts")
    ax.set_ylabel("Taux de conversion")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f"{y:.0%}"))
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()