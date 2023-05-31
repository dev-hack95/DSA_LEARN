import pandas as pd
import openpyxl

data = {
    "elements": [
        {
            "brand": "urn:li:organizationBrand:11280505",
            "timeRange": {
                "start": 1537142400000,
                "end": 1537228800000
            }
        },
        {
            "brand": "urn:li:organizationBrand:11280505",
            "timeRange": {
                "start": 1537228800000,
                "end": 1537315200000
            }
        }
    ],
    "paging": {
        "count": 10,
        "start": 0,
        "links": []
    }
}

df = pd.DataFrame(data["elements"])
df.to_excel("Organization Brand Time-Bound Page Statistics.xlsx", index=False)

