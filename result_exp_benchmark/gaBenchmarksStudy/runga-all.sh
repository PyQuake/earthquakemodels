nohup ssh cluster9.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runga-2.sh &' &> trash &
nohup ssh cluster1.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runga-3-6.sh &' &> trash &
nohup ssh cluster2.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runga-7-10.sh &' &> trash &
nohup ssh cluster4.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runme-11-14.sh &' &> trash &
nohup ssh cluster5.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runme-15-18.sh &' &> trash &
nohup ssh cluster6.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runme-19-22.sh & ' &> trash &
nohup ssh cluster8.local 'cd mpi_projects/gaBenchmarksStudy; nohup sh runme-23-24.sh &' &> trash &

