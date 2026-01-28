import shutil
import datetime
source="/Users/VEDHA/OneDrive/Desktop/Data and AI/data.txt"
backup = f"/Users/VEDHA/OneDrive/Desktop/Data and AI/data_backup_{datetime.date.today()}.txt"
shutil.copy(source,backup)
print(f"Backup of {source} created at {backup}")