nohup ssh cluster1.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme1-3.sh &' &> trash &
nohup ssh cluster2.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme4-6.sh &' &> trash &
nohup ssh cluster4.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme7-9.sh &' &> trash &
nohup ssh cluster5.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme10-12.sh & ' &> trash &
nohup ssh cluster6.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme13-15.sh &' &> trash &
nohup ssh cluster7.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme16-18.sh &' &> trash &
nohup ssh cluster8.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme19-21.sh &' &> trash &
nohup ssh cluster9.local 'cd mpi_projects/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy; nohup sh runme22-24.sh &' &> trash &