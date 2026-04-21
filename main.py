import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.dates as mdates

data = [
    ("Kick-off / Exposé-Anmeldung", "2026-04-22", "2026-04-22", "milestone"),
    ("Replikation BA Moritz Schäfer", "2026-04-22", "2026-04-30", "task"),
    ("Analyse OneWare Plugin-Architektur", "2026-04-27", "2026-05-08", "task"),
    ("Analyse OneWare UI-Stand", "2026-04-27", "2026-05-06", "task"),
    ("Replikation BA André Dolata", "2026-05-01", "2026-05-10", "task"),
    ("Einarbeitung GDB-Dokumentation", "2026-04-22", "2026-05-20", "task"),
    ("Analyse GDB-Schnittstelle auf Zielsystem", "2026-05-05", "2026-05-20", "task"),
    ("Entwurf Plugin- und Systemarchitektur", "2026-05-12", "2026-05-22", "task"),
    ("Dokumentation Projektanforderungen", "2026-04-22", "2026-05-22", "task"),
    ("Exposé-Abgabe", "2026-05-22", "2026-05-22", "milestone"),
    ("Exposé-Verteidigung", "2026-05-27", "2026-05-27", "milestone"),
    #("Umzug", "2026-06-01", "2026-06-14", "task"),
    ("Anmeldung Bachelorarbeit", "2026-06-14", "2026-06-14", "milestone"),
    ("Einarbeitung C#", "2026-06-15", "2026-06-28", "task"),
    ("Implementierung GDB-Start- und Steuerungsmodul", "2026-06-22", "2026-07-19", "task"),
    ("Implementierung Debug-UI", "2026-07-06", "2026-08-02", "task"),
    ("Integration in OneWare", "2026-07-27", "2026-08-23", "task"),
    ("Test mit SVNR / FPGA", "2026-08-17", "2026-09-06", "task"),
    ("Dokumentation Umsetzung und Entscheidungen", "2026-06-15", "2026-09-14", "task"),
    ("Abgabe Bachelorarbeit", "2026-09-14", "2026-09-14", "milestone"),
    ("Kolloquium", "2026-09-21", "2026-09-21", "milestone"),
]


df = pd.DataFrame(data, columns=["task", "start", "end", "type"])
df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])
df["duration"] = (df["end"] - df["start"]).dt.days

fig, ax = plt.subplots(figsize=(16, 10))

y_pos = np.arange(len(df))

for i, row in df.iterrows():
    if row["type"] == "task":
        ax.barh(
            i,
            row["duration"] if row["duration"] > 0 else 1,
            left=row["start"],
            height=0.6,
            align="center"
        )
    else:
        ax.scatter(
            row["start"],
            i,
            s=120,
            marker="D",
            zorder=3
        )

ax.set_yticks(y_pos)
ax.set_yticklabels(df["task"])
ax.invert_yaxis()

ax.axvline(
    pd.to_datetime("2026-04-22"),
    linestyle="--",
    linewidth=1.5
)

ax.text(
    pd.to_datetime("2026-04-22"),
    -0.8,
    "Kick-off / Exposé-Anmeldung",
    verticalalignment="bottom"
)


ax.set_xlim(pd.to_datetime("2026-04-20"), pd.to_datetime("2026-09-28"))

ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("KW %V\n%d.%m.%Y"))

ax.set_xlabel("Kalenderwochen")
ax.set_title("Projektplanung Bachelorprojekt: Debug-Plugin für SVNR in OneWare")

plt.xticks(rotation=45)
plt.grid(True, axis="x")
plt.tight_layout()
plt.show()