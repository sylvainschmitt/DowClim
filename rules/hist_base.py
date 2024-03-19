rule hist_base:
    input:
        "results/baselines/{area}_{base}_{aggregation}_{period_eval}.nc",
        "results/areas/{area}.shp"
    output:
        "results/evaluation/hist/base/{area}_{base}_{aggregation}_{period_eval}.tsv"
    log:
        "results/logs/hist_base_{area}_{base}_{aggregation}_{period_eval}.log"
    benchmark:
        "results/benchmarks/hist_base_{area}_{base}_{aggregation}_{period_eval}.benchmark.txt"
    threads: 1
    params:
      area="{area}",
      origin="{base}",
      domain="none",
      institute="none",
      model="none",
      experiment="none",
      ensemble="none",
      rcm="none",
      downscaling="none",
      base="none",
      aggregation="{aggregation}",
      period_proj="none",
      period_eval="{period_eval}",
      ds_method="none"
    script:
      "../scripts/hist_base.py"
