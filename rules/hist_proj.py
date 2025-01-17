rule hist_proj:
    input:
        "results/downscaled/{area}_{project}_{domain}_{institute}_{model}_{experiment}_{ensemble}_{rcm}_{downscaling}_{base}_{aggregation}_{period_proj}_{period_eval}_{ds_method}.nc",
        "results/areas/{area}.shp"
    output:
        temp("results/evaluation/hist/proj/{area}_{project}_{domain}_{institute}_{model}_{experiment}_{ensemble}_{rcm}_{downscaling}_{base}_{aggregation}_{period_proj}_{period_eval}_{ds_method}.tsv")
    log:
        "results/logs/hist_proj_{area}_{project}_{domain}_{institute}_{model}_{experiment}_{ensemble}_{rcm}_{downscaling}_{base}_{aggregation}_{period_proj}_{period_eval}_{ds_method}.log"
    benchmark:
        "results/benchmarks/hist_ds_{area}_{project}_{domain}_{institute}_{model}_{experiment}_{ensemble}_{rcm}_{downscaling}_{base}_{aggregation}_{period_proj}_{period_eval}_{ds_method}.benchmark.txt"
    threads: 1
    conda:
        "../envs/xarray.yml"
    params:
      area="{area}",
      origin="{project}",
      domain="{domain}",
      institute="{institute}",
      model="{model}",
      experiment="{experiment}",
      ensemble="{ensemble}",
      rcm="{rcm}",
      downscaling="{downscaling}",
      base="{base}",
      aggregation="{aggregation}",
      period_proj="{period_proj}",
      period_eval="{period_eval}",
      ds_method="{ds_method}"
    script:
      "../scripts/hist_proj.py"
