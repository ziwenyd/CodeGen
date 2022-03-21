https://console.cloud.google.com/bigquery?project=noted-cider-344618&ws=!1m25!1m4!4m3!1sbigquery-public-data!2sgithub_repos!3ssample_repos!1m4!4m3!1sbigquery-public-data!2sgithub_repos!3ssample_files!1m4!4m3!1sbigquery-public-data!2sgithub_repos!3ssample_contents!1m4!4m3!1sbigquery-public-data!2sgithub_repos!3sfiles!1m4!4m3!1sbigquery-public-data!2sgithub_repos!3scontents!1m5!1m4!1m3!1snoted-cider-344618!2sbquxjob_56a90d6d_17fa3b9c89d!3sUS&d=github_repos&p=bigquery-public-data&page=table&t=sample_contents


SQL QUERY:
```
SELECT sample_repo_name, sample_ref, sample_path, content  
FROM `bigquery-public-data.github_repos.sample_contents` 
WHERE ENDS_WITH(sample_path, '.py')

LIMIT 500
```
compress json files into a json.gz folder
for example
bash ```
~/Desktop/CodeGen/my_data/raw$ tar -zcvf python.000.json.gz python_raw_500.json
```
this will crate a folder `python.000.json.gz` containing one file named as `python.000.json` which has the same content as the python_raw_500.json