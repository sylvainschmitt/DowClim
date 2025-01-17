rule merge_eval:
    input:
      expand("results/evaluation/metrics/{proj}_{baseline}_{aggregation}_{period_eval}_{period_base}_{ds_method}_{base_eval}.tsv",
              proj=proj_dom.id,
              baseline=config["baseline"],
              aggregation=config["aggregation"],
              period_base=config["hist_years"],
              period_eval=config["eval_years"],
              ds_method=config["ds_method"],
              base_eval=config["base_eval"])
    output:
      "results/evaluation/evaluations.tsv"
    log:
      "results/logs/merge_eval.log"
    benchmark:
      "results/benchmarks/merge_eval.benchmark.txt"
    conda:
      "../envs/xarray.yml"
    script:
      "../scripts/merge_eval.py"
