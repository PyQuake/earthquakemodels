nohup ssh cluster1.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme1-4-pseudo-adaptative.sh &' &> trash &
nohup ssh cluster2.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme5-8-pseudo-adaptative.sh &' &> trash &
nohup ssh cluster4.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme9-12-pseudo-adaptative.sh &' &> trash &
nohup ssh cluster5.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme13-16-pseudo-adaptative.sh &' &> trash &
nohup ssh cluster6.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme17-20-pseudo-adaptative.sh &' &> trash &
nohup ssh cluster7.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme21-24-pseudo-adaptative.sh &' &> trash &