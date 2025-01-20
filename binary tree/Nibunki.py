from pynput.keyboard import Key, Listener
import os, time
'''
 █▄▄▀▀▀▀█      ▄▀  ▀▄        █    
             ▄█▄▄▄▄▄▄█▄  ▄▄▄▄█▄▄▄▄
           ▀▀  █    █  ▀   ▄▀█▀▄  
█▄▄▄▀▀▀▀▀█   ▄█   ▄▄▀    ▄▀  █  ▀▄
    Ni          Bun          Ki   
'''
os.system('color')
os.system(f'mode con: cols=165 lines=40')

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # create nodes
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None: self.left = Node(data)
                else: self.left.insert(data)
            elif data > self.data:
                if self.right is None: self.right = Node(data)
                else: self.right.insert(data)
        else:
            self.data = data
    # return tree
    def returnTree(self):
        self.tree_list = []
        self.__listTree(self)
        return self.tree_list
    def __listTree(self, root):
        line = [root]
        while len(line) > 0:
            current = line.pop(0)
            self.tree_list.append(current.data)
            if current.left != None: line.append(current.left)
            if current.right != None: line.append(current.right)
class Solution:
    def root(self, root):
        return root.data
    def edge(self, root):
        return self.__numberofnodes(root) - 1
    def __numberofnodes(self, root):
        if root == None: return 0
        return 1 + self.__numberofnodes(root.left) + self.__numberofnodes(root.right)
    def nodes(self, root, *, include = 'ALL'):
        self.nodesdict = {'root':root.data, 'other':[], 'leaf':[]}
        self.__nodesdict(root)
        if include == 'ALL': return self.nodesdict
        else: return self.nodesdict[include]
    def __nodesdict(self, root):
        if root.left == None and root.right == None:
            self.nodesdict['leaf'].append(root.data)
            return
        else:
            if root.data != self.nodesdict['root']:
                self.nodesdict['other'].append(root.data)
        if root.left != None: self.__nodesdict(root.left)
        if root.right != None: self.__nodesdict(root.right)
    def siblings(self, root):
        self.siblinglist = []
        self.__siblingslist(root)
        return self.siblinglist
    def __siblingslist(self, root):
        if root.left != None and root.right != None:
            self.siblinglist.append([root.left.data, root.right.data])
        if root.left != None: self.__siblingslist(root.left)
        if root.right != None: self.__siblingslist(root.right)
    def level(self, root, level = 0):
        if root.left == None and root.right == None: return level
        if root.left != None: left = self.level(root.left, level+1)
        if root.right != None: right = self.level(root.right, level+1)
        if root.left != None and root.right != None: return max(left, right)
        if root.left != None: return left
        if root.right != None: return right
    def height(self, root, height = 0):
        if root.left == None and root.right == None: return height
        if root.left != None: left = self.height(root.left, height)
        if root.right != None: right = self.height(root.right, height)
        if root.left != None and root.right != None: return max(left+1, right+1)
        if root.left != None: return left + 1
        if root.right != None: return right + 1
    def retrievePaths(self, root):
        self.allpaths = []
        path = []
        self.__retrievePathsRec(root, path, 0)
        return self.allpaths
    def __retrievePathsRec(self, root, path, pathLen):
        
        if(len(path) > pathLen): path[pathLen] = root.data
        else: path.append(root.data)

        pathLen = pathLen + 1
    
        if root.left == None and root.right == None: self.allpaths.append(' > '.join(path[:pathLen]))
        else:
            if root.left != None: self.__retrievePathsRec(root.left, path, pathLen)
            if root.right!= None: self.__retrievePathsRec(root.right, path, pathLen)
    def degreedict(self, root):
        self.degrees = {}
        self.__degreedict(root)
        arrangement = root.returnTree()
        return [f'{key} = {self.degrees[key]}' for key in arrangement]
    def __degreedict(self, root):
        if root.left == None and root.right == None: self.degrees[root.data] = 0
        elif root.left == None or root.right == None: self.degrees[root.data] = 1
        else: self.degrees[root.data] = 2
        if root.left != None: self.__degreedict(root.left)
        if root.right != None: self.__degreedict(root.right)
def MainMenu():
    '''helper function for Menu()'''
    for i in range(1, 7):
        Menu(i)
        time.sleep(.2)
def Menu(frame):
    cyan = "\033[1;36;40m"
    white = "\033[1;37;40m"
    green = "\033[1;32;40m"
    red = "\033[1;31;40m"
    magenta = "\033[1;35;40m"
    yellow = "\033[1;33;40m"
    gray = "\033[1;30;40m"
    os.system(f'mode con: cols=165 lines=40')
    menu6 = (f'''{cyan}                      ██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██   {cyan}
{cyan}                      █ ▀▄                                                                                                               ▄▀ █   {cyan}
{cyan}                      █   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   █   {cyan}
{cyan}                      █   █                                                                                                             {cyan}█   █   
{cyan}                      █   █                                                                                                             {cyan}█   █   
{cyan}                      █   █                                                                  {'' if frame < 6 else green}██{white}                                         {cyan}█   █   
{cyan}                      █   █                                              {'' if frame < 6 else green}▄██             ▄██▀{white} {'' if frame < 6 else red}▄▄█▄▄{white}                                     {cyan}█   █   
{cyan}                      █   █                                         {'' if frame < 6 else red}▄▄█▄▄{white}                     {'' if frame < 6 else red}║   ║{white}                                     {cyan}█   █   
{cyan}                      █   █                                         {'' if frame < 6 else red}║   ║{white}   {'' if frame < 6 else green}██         ██{white}     {'' if frame < 6 else red}▀▀▀▀▀{white}        {'' if frame < 6 else green}▄██{white}                          {cyan}█   █   
{cyan}                      █   █                         {'' if frame < 6 else green}▄██{white}             {'' if frame < 6 else red}▀▀▀▀▀{white}    {'' if frame < 6 else green}▀██                        ██▀     ██{white}                      {cyan}█   █  
{cyan}                      █   █                                                      {'' if frame < 6 else green}█▀ ██          ██▄  ██▀{white}      {'' if frame < 6 else red}▄▄█▄▄{white}                     {cyan}█   █   
{cyan}                      █   █                      {'' if frame < 6 else red}▄▄█▄▄{white}   {'' if frame < 6 else green}▀██                  ██▀      ██{white}                     {'' if frame < 6 else red}║   ║{white}          {'' if frame < 6 else green}▄██{white}        {cyan}█   █   
{cyan}                      █   █         {'' if frame < 6 else green}██▄{white}          {'' if frame < 6 else red}║   ║{white}        {'' if frame < 6 else green}▀██        ██▀{white}          {'' if frame < 6 else red}▄▄█▄▄{white}        {'' if frame < 6 else green}██▄{white}        {'' if frame < 6 else red}▀▀▀▀▀{white}                     {cyan}█   █   
{cyan}                      █   █                      {'' if frame < 6 else red}▀▀▀▀▀{white}                {'' if frame < 6 else green}██▀{white}             {'' if frame < 6 else red}║   ║{white}           {'' if frame < 6 else green}██▄               ██▄{white}             {cyan}█   █  
{cyan}                      █   █           {'' if frame < 6 else green}▀██                          ▀██{white}                {'' if frame < 6 else red}▀▀▀▀▀{white}                       {'' if frame < 6 else green}██▀         ██▄{white}       {cyan}█   █  
{cyan}                      █   █       {'' if frame < 6 else green}▄██▀    ▀██                           ▀██  ▄██                         ██▀{white}                 {'' if frame < 6 else red}▄▄█▄▄{white}      {cyan}█   █   
{cyan}                      █   █      {'' if frame < 5 else red}▄▄█▄▄{white}      {'' if frame < 5 else green}▀██         ██{white}                                                                   {'' if frame < 5 else red}║   ║{white}      {cyan}█   █   
{cyan}                      █   █      {'' if frame < 5 else red}║   ║{white}               {'' if frame < 5 else green}██{white}                 {'' if frame < 5 else red}▄▄█▄▄{white}      {'' if frame < 5 else green}██     ▄██▀   ██{white}                          {'' if frame < 5 else red}▀▀▀▀▀{white}      {cyan}█   █ 
{cyan}                      █   █      {'' if frame < 5 else red}▀▀▀▀▀{white}           {'' if frame < 5 else green}▀██{white}                    {'' if frame < 5 else red}║   ║{white}                                                           {cyan}█   █    
{cyan}                      █   █                           {'' if frame < 5 else green}██    ▀██{white}         {'' if frame < 5 else red}▀▀▀▀▀{white}          {'' if frame < 5 else green}▄██{white}     {'' if frame < 5 else red}▄▄█▄▄{white}             {'' if frame < 5 else green}██       ██▄{white}           {cyan}█   █  
{cyan}                      █   █                                      {'' if frame < 5 else green}▀██▄              ▄██▀{white}        {'' if frame < 5 else red}║   ║{white}                 {'' if frame < 5 else green}██▀        ██▄{white}     {cyan}█   █   
{cyan}                      █   █                    {'' if frame < 5 else green}▄██▄                   ▀██▄                     {'' if frame < 5 else red}▀▀▀▀▀{white}      {'' if frame < 5 else green}██▀{white}                           {cyan}█   █   
{cyan}                      █   █             {'' if frame < 4 else green}██▀{white}                  {'' if frame < 4 else red}▄▄█▄▄{white}        {'' if frame < 4 else green}▀██    ▄██               ██▀          ██▄        ██▀{white}          {cyan}█   █   
{cyan}                      █   █                                  {'' if frame < 4 else red}║   ║{white}           {'' if frame < 4 else green}▀██           ▄██▀{white}                 {'' if frame < 4 else red}▄▄█▄▄{white}                   {cyan}█   █   {cyan}
{cyan}                      █   █                     {'' if frame < 4 else green}██{white}           {'' if frame < 4 else red}▀▀▀▀▀{white}             {'' if frame < 4 else green}▀██   ██▀{white}                        {'' if frame < 4 else red}║   ║{white}        {magenta}█▄▄▀▀▀▀█   {cyan}█   █   
{cyan}                      █   █                                                      {'' if frame < 4 else green}▀██{white}                            {'' if frame < 4 else red}▀▀▀▀▀{white}                   {cyan}█   █   
{cyan}                      █   █                                                      {'' if frame < 3 else gray}██{white}                                         {magenta}█▄▄▄▀▀▀▀▀█  {cyan}█   █   
{cyan}                      █   █                                                     {'' if frame < 3 else gray}████{white}                                                    {cyan}█   █   
{cyan}                      █   █                                                    {'' if frame < 2 else yellow}▀█████▄{white}                                       {'' if frame < 2 else yellow}▄▀  ▀▄     {cyan}█   █
{cyan}                      █   █                                                     {'' if frame < 2 else yellow}▄██████▄{white}                                   {'' if frame < 2 else yellow}▄█▄▄▄▄▄▄█▄   {cyan}█   █
{cyan}                      █   █                                                   {'' if frame < 2 else yellow}▄████████▄{white}                                 {'' if frame < 2 else yellow}▀▀  █    █  ▀  {cyan}█   █
{cyan}                      █   █                                                 {'' if frame < 2 else yellow}▄████████████▄{white}                                 {'' if frame < 2 else yellow}▄█   ▄▄▀     {cyan}█   █
{cyan}                      █   █                                                {magenta}▄████████████▀{white}                                        {'' if frame < 3 else green}▄      {cyan}█   █  
{cyan}                      █   █                                                {magenta}██████████████▄{white}                                   {'' if frame < 3 else green}▄▄▄▄█▄▄▄▄  {cyan}█   █   
{cyan}                      █   █                                              {magenta}▄██████████████████▄{white}                                  {'' if frame < 3 else green}▄▀█▀▄    {cyan}█   █  
{cyan}                      █   █                                           {magenta}▄██████████████████████▄{white}  Click Enter to continue...   {'' if frame < 3 else green}▄▀  █  ▀▄  {cyan}█   █  
{cyan}                      █   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   █{cyan}
{cyan}                      █ ▄▀                                                                                                               ▀▄ █{cyan}
{cyan}                      ██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██{cyan}   ''')
    print(menu6)
def TreeDisplay(nodes, arrangement, treedata):
    os.system(f'mode con: cols=165 lines=40')
    cyan = "\033[1;36;40m"
    white = "\033[1;37;40m"
    green = "\033[1;32;40m"
    red = "\033[1;31;40m"
    magenta = "\033[1;35;40m"
    contents = list(''.join(arrangement).ljust(20))
    slider = "◂ "+("="*(nodes-10))+"██"+("="*(10-(nodes-10)))+" ▸"
    tree = (f'''{cyan}██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██   {green}██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██
{cyan}█ ▀▄                                                                                                               ▄▀ █   {green}█ ▀▄                                   ▄▀ █
{cyan}█   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   █   {green}█   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   █
{cyan}█   █                                         {green}▄▄▄▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄▄{white}                                         {cyan}█   █   {green}█   █ ROOT: {treedata['root']}                         █   █
{cyan}█   █                               {green}▄▄▄▄▀▀▀▀▀▀{white}  {red}▄▄▄▄▄{white}                    {green}▀▀▀▀▀▀▄▄▄▄{white}                               {cyan}█   █   {green}█   █ EDGE: {treedata['edge']}                        █   █
{cyan}█   █                         {green}▄▄▄▀▀▀{white}   ╔════════{red}║ {contents[0]} ╠{white}══════╗       {red}▄▄▄▄▄{white}           {green}▀▀▀▄▄▄{white}                         {cyan}█   █   {green}█   █ PARENT: {treedata['parent'][0]}   █   █
{cyan}█   █                     {green}▄▄▀▀{white}     ╔═══╝        {red}▀▀▀▀▀{white}      ╚═══════{red}╣ {contents[2]} ║{white}                 {green}▀▀▄▄{white}                     {cyan}█   █   {green}█   █         {treedata['parent'][1]}   █   █
{cyan}█   █                  {green}▄▄▀{white}      ╔══╝                               {red}▀▀█▀▀ {white}                    {green}▀▄▄{white}                  {cyan}█   █   {green}█   █         {treedata['parent'][2]}   █   █
{cyan}█   █               {green}▄▄▀{white}      ╔══╝        {red}▄▄▄▄▄{white}                       ╠══════════════╗           {green}▀▄▄{white}               {cyan}█   █   {green}█   █ CHILD:  {treedata['child'][0]}   █   █
{cyan}█   █           {green}▄▄▀▀{white}      ╔══╝           {red}║ {contents[5]} ╠{white}═══════════════════════╝              ║              {green}▀▀▄▄{white}           {cyan}█   █   {green}█   █         {treedata['child'][1]}   █   █
{cyan}█   █         {green}▄▀{white}       ╔══╝              {red}{"▀▀█▀▀" if nodes >= 12 else "▀▀▀▀▀"}{white}                                    {red}▄▄█▄▄{white}                {green}▀▄{white}         {cyan}█   █   {green}█   █         {treedata['child'][2]}   █   █
{cyan}█   █       {green}▄▀{white}         ║                   {"╚══════════╗" if nodes >= 12 else " "*12}      {red}{"▄▄▄▄▄" if nodes >= 13 else " "*5}{white}                {red}║ {contents[6]} {f"╠{white}══════╗" if nodes >= 15 else "║"+" "*7}           {green}▀▄{white}       {cyan}█   █   {green}█   █ SIBLINGS: {treedata['sibling'][0]}       █   █
{cyan}█   █     {green}▄▀{white}         {red}▄▄█▄▄{white}                            {"╠" if nodes >= 13 else "║" if nodes >= 12 else " "}{f"══════{red}║ {contents[12]} ║" if nodes >= 13 else " "*11}{white}                {red}{"▀▀█▀▀" if nodes >= 14 else "▀▀▀▀▀"}{white}      {"║" if nodes >= 15 else " "}             {green}▀▄{white}     {cyan}█   █   {green}█   █           {treedata['sibling'][1]}       █   █
{cyan}█   █    {green}▄▀{white}          {red}║ {contents[1]} ╠{white}════════════════════╗       {"╚═╗" if nodes >= 12 else " "*3}    {red}{"▀▀▀▀▀" if nodes >= 13 else " "*5}{white}                  {"╚═╗" if nodes >= 14 else " "*3}      {"║" if nodes >= 15 else " "}     {red}{"▄▄▄▄▄" if nodes >= 15 else " "*5}{white}    {green}▀▄{white}    {cyan}█   █   {green}█   █           {treedata['sibling'][2]}         █   █
{cyan}█   █   {green}▄▀{white}           {red}▀▀█▀▀{white}                    ║         {"╚╗" if nodes >= 12 else "  "}                            {"║" if nodes >= 14 else " "}      {f"╚═════{red}╣ {contents[14]} ║" if nodes >= 15 else " "*11}{white}     {green}▀▄{white}   {cyan}█   █   {green}█   █ LEAF: {treedata['leaf'][0]}  █   █
{cyan}█   █   {green}█{white}              ║                      ╚══════╗   {"╚════════╗" if nodes >= 12 else " "*10}        {red}{"▄▄▄▄▄" if nodes >= 12 else " "*5}{white}      {"║" if nodes >= 14 else " "}            {red}{"▀▀▀▀▀" if nodes >= 15 else " "*5}{white}      {green}█{white}   {cyan}█   █   {green}█   █       {treedata['leaf'][1]}  █   █
{cyan}█   █  {green}█{white}               ║           {red}▄▄▄▄▄{white}             ║            {f"╚════════{red}╣ {contents[11]} ║" if nodes >= 12 else " "*14}{white}      {"║" if nodes >= 14 else " "}                        {green}█{white}  {cyan}█   █   {green}█   █ DEGREE: {treedata['degree'][0]}   █   █
{cyan}█   █ {green}█{white}                ╚═══════════{red}╣ {contents[3]} ╠{white}══╗        {red}▄▄█▄▄{white}                   {red}{"▀▀▀▀▀" if nodes >= 12 else " "*5}{white}      {"╚════════╗" if nodes >= 14 else " "*10}                {green}█{white} {cyan}█   █   {green}█   █         {treedata['degree'][1]}   █   █
{cyan}█   █ {green}█{white}                            {red}▀▀█▀▀{white}  ║        {red}║ {contents[4]} {f"╠{white}════════╗" if nodes >= 11 else "║"+" "*9}                              {"║" if nodes >= 14 else " "}                {green}█{white} {cyan}█   █   {green}█   █         {treedata['degree'][2]}   █   █
{cyan}█   █  {green}█{white}                   {red}▄▄▄▄▄{white}    ╔╝    ║        {red}▀▀█▀▀{white}        {"╚════════╗" if nodes >= 11 else " "*10}                     {"║" if nodes >= 14 else " "}               {green}█{white}  {cyan}█   █   {green}█   █         {treedata['degree'][3]}   █   █
{cyan}█   █   {green}█{white}          {f"╔═══════{red}╣" if nodes >= 16 else (" "*8)+f"{red}║"} {contents[7]} ╠{white}════╝     ║          ║                   {"║" if nodes >= 11 else " "}                   {red}{"▄▄█▄▄" if nodes >= 14 else " "*5}{white}            {green}█{white}   {cyan}█   █   {green}█   █         {treedata['degree'][4]}   █   █
{cyan}█   █   {green}▀▄{white}         {"║" if nodes >= 16 else " "}       {red}{"▀▀█▀▀" if nodes >= 17 else "▀▀▀▀▀"}{white}        {red}▄▄█▄▄{white}        ╚══╗              {red}{"▄▄█▄▄" if nodes >= 11 else " "*5}{white}                 {red}{f"║ {contents[13]} ║" if nodes >= 14 else " "*5}{white}           {green}▄▀{white}   {cyan}█   █   {green}█   █         {treedata['degree'][5]}   █   █
{cyan}█   █    {green}▀▄{white}      {red}{"▄▄█▄▄" if nodes >= 16 else " "*5}{white}       {"║" if nodes >= 17 else " "}          {red}║ {contents[8]} {f"╠{white}═══╗" if nodes >= 19 else f"║{white}"+" "*4}       ║   {red}▄▄▄▄▄{white}      {red}{f"║ {contents[10]} ║" if nodes >= 11 else " "*5}{white}                 {red}{"▀▀▀▀▀" if nodes >= 14 else " "*5}{white}          {green}▄▀{white}    {cyan}█   █   {green}█   █         {treedata['degree'][6]}   █   █
{cyan}█   █     {green}▀▄{white}     {red}{f"║ {contents[15]} ║" if nodes >= 16 else " "*5}{white}     {"╔═╝" if nodes >= 17 else " "*3}          {red}{"▀▀█▀▀" if nodes >= 18 else "▀▀▀▀▀"}{white}   {"╚═╗" if nodes >= 19 else " "*3}     ╚═══{red}╣ {contents[9]} ║{white}      {red}{"▀▀▀▀▀" if nodes >= 11 else " "*5}{white}                               {green}▄▀{white}     {cyan}█   █   {green}█   █ LEVEL: {treedata['level']}                        █   █
{cyan}█   █       {green}▀▄{white}   {red}{"▀▀▀▀▀" if nodes >= 16 else " "*5}{white}     {"║" if nodes >= 17 else " "}              {"║" if nodes >= 18 else " "}       {"║" if nodes >= 19 else " "}         {red}{"▀▀█▀▀" if nodes >= 20 else "▀▀▀▀▀"}{white}                                        {green}▄▀{white}       {cyan}█   █   {green}█   █ PATHS: {treedata['path'][0]}        █   █
{cyan}█   █         {green}▀▄{white}         {red}{"▄▄█▄▄" if nodes >= 17 else " "*5}{white}            {"╚══╗" if nodes >= 18 else " "*4}    {"╚══╗" if nodes >= 19 else " "*4}        {"╚═══════╗" if nodes >= 20 else " "*9}        {red}{"▄▄▄▄▄" if nodes >= 20 else " "*5}{white}                   {green}▄▀{white}         {cyan}█   █   {green}█   █        {treedata['path'][1]}        █   █
{cyan}█   █           {green}▀▄{white}       {red}{f"║ {contents[16]} ║" if nodes >= 17 else " "*5}{white}             {red}{"▄▄█▄▄" if nodes >= 18 else " "*5}{white}     {"╚═════╗" if nodes >= 19 else " "*7}          {f"╚════════{red}╣ {contents[19]} ║" if nodes >= 20 else " "*14}{white}                 {green}▄▀{white}           {cyan}█   █   {green}█   █        {treedata['path'][2]}        █   █
{cyan}█   █             {green}▀▄{white}     {red}{"▀▀▀▀▀" if nodes >= 17 else " "*5}{white}             {red}{f"║ {contents[17]} ║" if nodes >= 18 else " "*5}{white}         {red}{"▄▄█▄▄" if nodes >= 19 else " "*5}{white}                 {red}{"▀▀▀▀▀" if nodes >= 20 else " "*5}{white}               {green}▄▀{white}             {cyan}█   █   {green}█   █        {treedata['path'][3]}        █   █
{cyan}█   █               {green}▀▀▄▄▄▄{white}                 {red}{"▀▀▀▀▀" if nodes >= 18 else " "*5}{white}         {red}{f"║ {contents[18]} ║" if nodes >= 19 else " "*5}{white}                               {green}▄▄▄▄▀▀{white}               {cyan}█   █   {green}█   █        {treedata['path'][4]}        █   █
{cyan}█   █                     {green}▀▀▀▀▄▄▄▄▄▄▄▄{white}                   {red}{"▀▀▀▀▀" if nodes >= 19 else " "*5}{white}                   {green}▄▄▄▄▄▄▄▄▀▀▀▀{white}                     {cyan}█   █   {green}█   █        {treedata['path'][5]}        █   █
{cyan}█   █                                 {green}▀▀▀▀▀▀▀▀▄▄▄▄{white}                   {green}▄▄▄▄▀▀▀▀▀▀▀▀{white}                                 {cyan}█   █   {green}█   █        {treedata['path'][6]}        █   █
{cyan}█   █                                            {white}█{white}   {green}▀▀▀▀▀▀▀▀  ▄▄▄▄▄▀{white}          {magenta}██▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀██{white}   {cyan}█   █   {green}█   █        {treedata['path'][7]}        █   █
{cyan}█   █                                            {white}█{white}               {white}▄▀{white}            {magenta}█ ▀          NODE #          ▀ █{white}   {cyan}█   █   {green}█   █        {treedata['path'][8]}        █   █
{cyan}█   █                                             {white}█{white}             {white}█{white}              {magenta}█              {str(nodes).ljust(2)}              █{white}   {cyan}█   █   {green}█   █        {treedata['path'][9]}        █   █
{cyan}█   █                                            {white}█{white}             {white}█{white}               {magenta}█ ▄     {slider}     ▄ █{white}   {cyan}█   █   {green}█   █ HEIGHT: {treedata['height']}                       █   █
{cyan}█   █                                          {white}▄▀{white}             {white}▀▄{white}               {magenta}██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██{white}   {cyan}█   █   {green}█   █ DEPTH:  {treedata['depth']}                       █   █
{cyan}█   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   █   {green}█   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   █
{cyan}█ ▄▀                                                                                                               ▀▄ █   {green}█ ▄▀                                   ▀▄ █
{cyan}██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██   {green}██▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄██''')
    print(tree)
def GenerateData(added_from_ten):
    os.system('cls')
    contents = ["GDIBFHJACE", "HDJBFIKACEG", "HDKBFJLACEGI", "HDLBFJMACEGIK",
    "HDLBFJNACEGIKM", "HDLBFJNACEGIKMO", "IEMCGKOBDFHJLNPA",
    "JFNDHLPBEGIKMOQAC", "KGODIMQBFHJLNPRACE", "LHPDJNRBFIKMOQSACEG",
    "MHQDKOSBFJLNPRTACEGI"][added_from_ten]
    root = Node(contents[0])
    for i in contents[1:]: root.insert(i)
    treedata = {'root':Solution().root(root), 'edge':str(Solution().edge(root)).ljust(2)}
    nodes = Solution().nodes(root)
    parents = ', '.join([nodes['root']]+nodes['other']).ljust(63)
    parents = [parents[:21], parents[21:42], parents[42:]]
    treedata['parent'] = parents
    child = ', '.join(nodes['other']+nodes['leaf']).ljust(63)
    child = [child[:21], child[21:42], child[42:]]
    treedata['child'] = child
    siblings_combined = ['&'.join(i) for i in Solution().siblings(root)]
    siblings_combined = [(', '.join(siblings_combined[:3]) + ', ').ljust(15), (', '.join(siblings_combined[3:6]) + ', ').ljust(15), (', '.join(siblings_combined[6:])).ljust(13)]
    treedata['sibling'] = siblings_combined
    leaf = ', '.join(nodes['leaf']).ljust(48)
    leaf = [leaf[:24], leaf[24:]]
    treedata['leaf'] = leaf
    degree = ', '.join(Solution().degreedict(root)).ljust(147)
    degree = [degree[:21], degree[21:42], degree[42:63], degree[63:84], degree[84:105], degree[105:126], degree[126:]]
    treedata['degree'] = degree
    treedata['level'] = Solution().level(root)
    path = Solution().retrievePaths(root)
    treedata['path'] = [i.ljust(17) for i in path] + [' '*17]*(10-len(path))
    treedata['height'] = Solution().height(root)
    treedata['depth'] = Solution().level(root)
    TreeDisplay(added_from_ten+10, root.returnTree(), treedata)
def on_press(key):
    global added_from_ten, screen_state

    if key == Key.left and screen_state == 'TREE':
        if added_from_ten > 0: added_from_ten -= 1
        GenerateData(added_from_ten)
    if key == Key.right and screen_state == 'TREE':
        if added_from_ten < 10: added_from_ten += 1
        GenerateData(added_from_ten)
    if key == Key.esc and screen_state == 'TREE':
        print('EXIT')
        screen_state = 'MENU'
        added_from_ten = 0
        MainMenu()
    if key == Key.enter and screen_state == 'MENU':
        screen_state = 'TREE'
        GenerateData(added_from_ten)

MainMenu()
screen_state = 'MENU'
added_from_ten = 0
with Listener(on_press=on_press) as listener: listener.join()