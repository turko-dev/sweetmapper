<h1>SweetMapper 2.1</h1>
<p>SweetMapper is a project designed to source, compile, and organize detailed marketing information about physical businesses and places using the Google Places API. The project automates the retrieval of important business data, including email addresses, phone numbers, physical addresses, and photos, and stores this information in organized databases. These databases can be useful for marketers looking to cold approach businesses or for job-seekers who want to apply to specific companies.</p>
<p><b>Important Note: </b>As of now SweetMapper is only available for Linux Devices however, a Windows/Mac release is on the way.</p>

<h2>Installation</h2>
Sweetmapper is a single-script application which means that all the functionality is contained within a single .py file. The way you install Sweetmapper is by cloning the repository from this page and running python3 before the sweetmapper.py file.

<h4>Run the file</h4>

```console
python3 sweetmapper.py
```

<h2>Features</h2>
<ul>
  <li><b>Automated Business Data Collection:</b> Uses the Google Places API to source a list of physical businesses in specified geographic regions.</li>
  <li><b>Comprehensive Data Points:</b> Collects and compiles data such as business names, phone numbers, email addresses (if available), physical addresses, and images.</li>
  <li><b>Database Storage: </b>Organizes the collected information into structured databases for easy access and use.</li>
  <li><b>Flexible Use Cases:</b> Designed for both marketers seeking business leads for cold outreach and job-seekers looking for potential companies to apply to.</li>
  <li><b>Customizable Queries:</b> Allows users to specify location and business type to focus searches based on their needs.</li>
</ul>

<h2>Documentation</h2>

To access Sweetmapper, you must first issue an API Key from Google to use their API's. There is a free usage credit assigned to each Google Account per month and Sweetmapper will not use many credits regardless. However, if you wish to use Sweetmapper often, you may also have to pay Google a cut to use in large amounts.

```console
Enter Google Maps API Key (Must be 39 characters)
> ***************************************
```
You must first configure your search before searching for anything and can be done by pressing Option 1 (Configure Search)

```console
Welcome to Sweetmapper 2.0
1 - Configure Search
2 - Paste Results to CSV
3 - Print Results to Screen
4 - Do Both
5 - Exit
```



