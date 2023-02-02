import os
from pathlib import Path

import cartopy
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
from cartopy.io.img_tiles import OSM


def generate_map(center: tuple, output_path: Path) -> Path:
    zoom_level = int(os.getenv("MAP_CONFIG_ZOOM", 10))
    figsize = (
        int(os.getenv("MAP_CONFIG_FIGSIZE", 5)),
        int(os.getenv("MAP_CONFIG_FIGSIZE", 5)),
    )
    extent_margin = float(os.getenv("MAP_CONFIG_EXTENT_RELATIVE", 0.3))
    plt.subplots(figsize=figsize)
    ax = plt.axes(projection=cartopy.crs.PlateCarree())

    extent = [
        center[0] - extent_margin,
        center[0] + extent_margin,
        center[1] - extent_margin,
        center[1] + extent_margin,
    ]
    ax.set_extent(extent)
    ax.plot(
        center[0], center[1], "bo", markersize=2, transform=cartopy.crs.PlateCarree()
    )
    ax.text(
        center[0],
        center[1],
        f" lon: {center[0]}, lat: {center[1]}",
        transform=cartopy.crs.Geodetic(),
        size=3,
    )
    ax.add_image(OSM(), zoom_level)

    gl = ax.gridlines(
        draw_labels=True,
        linewidth=0.6,
        color="gray",
        alpha=0.1,
        linestyle="-.",
    )
    gl.xlabel_style = {"size": 3, "color": "gray"}
    gl.ylabel_style = {"size": 3, "color": "gray"}

    # remove border

    # ax.stock_img()
    output_filename = Path(output_path, "map.png")
    plt.savefig(output_filename, dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()


def main():
    generate_map((-0.4577, 47.1104), Path("/tmp"))
    exit()
    print(cartopy.__version__)

    elevation = 0
    opacity = 100

    zoom_level = 10
    center = (-0.4577, 47.1104)
    figsize = (10, 10)
    extent_margin = 0.3

    plt.subplots(figsize=figsize)
    ax = plt.axes(projection=cartopy.crs.PlateCarree())

    extent = [
        center[0] - extent_margin,
        center[0] + extent_margin,
        center[1] - extent_margin,
        center[1] + extent_margin,
    ]
    ax.set_extent(extent)
    ax.plot(
        center[0], center[1], "bo", markersize=7, transform=cartopy.crs.PlateCarree()
    )

    request = cimgt.Stamen(
        style="toner-lite"
    )  # cartopy.io.img_tiles.GoogleTiles(style="satellite")
    # request = cartopy.io.img_tiles.GoogleTiles(style="satellite")

    ax.add_image(OSM(), zoom_level)
    # ax.stock_img()
    plt.savefig("test.png", dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()


if __name__ == "__main__":
    main()
