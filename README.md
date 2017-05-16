# Ubiquiti AutoConfig Bots for Python

* Automated Point-to-Point Link Configuration with Ubiquiti Devices for Python.
* Simple use and modification.
* Includes runtime at the end of the process.

## Requirements

* Python 3.6.1 (https://www.python.org/)
* Selenium (pip install selenium)

## Execute

**Ubiquiti airMAX M v6:**

To configure "Point A" or "Access Point" for Point-to-Point:

	$ py ubnt_ptp_a.py

To configure "Point B" or "Station" for Point-to-Point:

	$ py ubnt_ptp_b.py

To configure "Client WISP":

	$ py ubnt_wisp_client.py

**Ubiquiti airMAX AC v7:**

To configure "Point A" or "Access Point" for Point-to-Point:

	$ py ubnt_ptp_ac_a.py

To configure "Point B" or "Station" for Point-to-Point:

	$ py ubnt_ptp_ac_b.py
	
**Ubiquiti airMAX AC v8:**

To configure "Point A" or "Access Point" for Point-to-Point:

	$ py ubnt_ptp_ac_a_v8.py

To configure "Point B" or "Station" for Point-to-Point:

	$ py ubnt_ptp_ac_b_v8.py

## Changelog

**v4.2** May 16, 2017
- Add disable-infobars.
- Add ubnt_wisp_client.py (airMAX M)

**v4.1** May 16, 2017
- Optimization: ubnt_ptp_a.py (airMAX M)
- Optimization: ubnt_ptp_b.py (airMAX M)

**v4.0** May 11, 2017
- Add ubnt_ptp_ac_a_v8.py (airMAX AC v8)
- Add ubnt_ptp_ac_b_v8.py (airMAX AC v8)

**v3.0** May 11, 2017
- Add ubnt_ptp_ac_a.py (airMAX AC v7)
- Add ubnt_ptp_ac_b.py (airMAX AC v7)

**v1.0** May 10, 2017
- Add ubnt_ptp_a.py (airMAX M)
- Add ubnt_ptp_b.py (airMAX M)

## License

Ubiquiti AutoConfig Bots for Python is [GPL-3.0](https://github.com/KRIPT4/Ubiquiti-AutoConfig-Bots-for-Python/blob/master/LICENSE) Licensed  
Copyright © 2017 KRIPT4 (https://github.com/KRIPT4)
