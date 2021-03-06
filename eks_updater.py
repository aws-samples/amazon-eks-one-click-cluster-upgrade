from eksupdate.starter import main
import argparse
if __name__ == "__main__":
    example_text = '''
example:

             python3 eks_updater.py Name_Of_Cluster new_Version Region


Force Pod Eviction when you Have Pdb (Pod disruption budget):

   -> python3 eks_updater.py Cluster_Name new_Version aws_Region --force 

Skip Vpc Cni Upgrade:

   -> python3 eks_updater.py Cluster_Name new_Version aws_Region --pass_vpc 

Skip Upgrade Work Flow:

   -> python3 eks_updater.py Cluster_Name new_Version aws_Region --preflight 

 ''' 
    regions_list=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']

    parser = argparse.ArgumentParser(description='Eks Cluster OneClick Upgrade',epilog=example_text,
                                 formatter_class=argparse.RawDescriptionHelpFormatter
                                )
    parser.add_argument("name", help="Cluster Name")
    parser.add_argument("version",help="new version which you want to update")
    parser.add_argument("region",help="Give the region name "+', '.join(regions_list))
    parser.add_argument('--pass_vpc', action="store_true", default=False,help='this --pass-vpc will skip the vpc cni upgrade')
    parser.add_argument("--max_retry",default=2,type=int,help="you can specify max retry or else by default it is 2")
    parser.add_argument("--force",action="store_true", default=False,help="force pod eviction when you have pdb")
    #Eksctl will be added in future version
    parser.add_argument("--eksctl",action="store_true", default=False,help="eksctl upgrade process")
    parser.add_argument("--preflight",action="store_true", default=False,help="Run preflight check without upgrade")
    parser.add_argument("--email",default = False , help='Email for sharing the preflight report')
    parser.add_argument("--parallel",action="store_true",default = False , help='Parllel Upgrade all node groups together ')
    args = parser.parse_args()
    main(args)

       