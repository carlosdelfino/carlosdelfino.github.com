---
title: "Um Estudo Comparativo Sobre SELinux e AppArmor" 
tags: [Linux, AppArmor, SELinux, MAC, DAC, Linux, Kernel, Segurança, Sistemas de Arquivos, Administração, Invasão]
categories: [LinuxWindowsMac]
layout: article
share: true
toc: true
comments: true
feature:
 category: true
 index: true
image:
 feature: linuxmacwindows/allOS-logos-900x210.png
 teaser: linuxmacwindows/macwindowslinux-500x210.png
ads: 
 show: true
tagcloud: true
coinbase:
 show: true
---

O estudo comparativo a seguir, é um trabalho relativo a disciplina *Administração Unix-Like* do curso de *Pós Graduação em Administração e Segurança de Sistemas Computacional*, este comparativo visa apresentar as diferenças básicas entre as ferramentas, com uma visão superficial de sua arquitetura.

<!--more-->

## Introdução

Apresentamos neste artigo duas ferramentas Linux que visam reduzir a zero o ataque ao sistema operacional por suas diversas opções de entrada e saída, controlando assim aplicações que fazem uso dos recursos do sistema operacional.

O conceito de Estruturas de Segurança envolve diversas ferramentas, porém iremos comparar apenas duas delas SELinux (Secure-Enhanced Linux) e AppArmor (Application Armor) que sem dúvida são as mais utilizadas e discutidas atualmente.

## Revisão Bibliográfica

Visando compreender o vocabulário usado neste artigo, e facilitando a leitura não somente por especialistas no campo de segurança, mas buscando auxiliar profissionais dos setores de tomada de decisão das mais diversas modalidade de empresas, abaixo está listado alguns termos que serão comumente vistos aqui.

 - DAC  
   Sistema de permissões padrão do Linux. (Discretionary Access Control, ou Controle Discricionário de Acesso). Nativo no Linux e representado em especial pelo comando chmod que altera os direitos e acesso para os três níveis de uso do arquivo, Usuário, Grupos e Outros.
 - LSM  
   Linux Security Module, uma infraestrutura que estabelece a arquitetura de módulos usadas para carregar novos serviços de segurança.
 - MAC 
   Mandatory Access Control, Controle obrigatório de Acesso.
 - NSA  
   National Security Agency - Agencia Nacional de Segurança, organização Norte Americana de Defesa Nacional.   


SElinux  teve sua origem na pesquisa realizada pela NSA juntamente com as empresas SCC (Secure Computing Corporation) e MITRE (MITRE COMPORTATION, uma organização sem fins lucrativos.), com o nome "Projeto Extravaganza" no inicio dos anos 90, conforme o tutorial [IBM-Part1-SELinux], nesta época não existia o Linux, e o projeto era destinado ao Sistema Operacionais de nome Mach em uma versão conhecida como DTMach criado para ambientes distribuídos, tendo em seguida como foco de desenvolvimento o sistema DTOS, era desenvolvido no National Information Assurance Research Laboratory, pelo grupo Truested Systems Research group [NCSA-TSRG], com a entrada da Universidade de Utah foi portado para o sistema operacional Fluke, com o nome de Flux. Em paralelo o NSA adotou a políticas de segurança mais dinâmicas e finalmente em 2000 assumiu o nome SELinux sendo portado e disponibilizado no Linux no Kernel 2.2.

Em paralelo AppArmor teve seu desenvolvimento iniciado em 1998 para o Immunix uma versão segura do linux, nesta época conhecido como SubDomain e era produzido pela empresa Wirex, conforme [AppArmor-History], contribuindo assim com a criação do LSM. Em 2005 Novell adquiriu o Immunix, renomeando SubDomain para AppArmor, reescrevendo todo o código readequando ao Kernel do Linux. Em 2009 AppArmor foi liberado como um módulo do kernel linux mais integrado ao LSM e finalmente em 2010 se tornou um módulo oficial do kernel 2.6.36.


## Aspectos de Segurança (Sobre os Softwares)

O SELinux, conforme [WorldLibrary-AppArmor], usa iNodes o que lhe dá
maior segurança, mesmo com a criação de hard-links, neste caso negando o acesso ao arquivo com base no novo iNode. Já o AppArmor tem seu profiles baseados no path do arquivo, sendo sujeito a falhas caso sejam criados links.

##  Comparativo

A tabela abaixo foi baseada em outra disponível em [suse-selinux-comparison], onde a empresa Novell responsável pela distribuição de mesmo nome, apresenta as diferenças entre as estruturas de segurança AppArmor e SELinux, considerando esta distribuição.

<figure>
<table class="table_comparison table_text">
                        <thead>
                            <tr>
                                <th class="null">&nbsp;</th>
                                <th><strong>AppArmor</strong></th>
                                <th class="last-child"><strong>SELinux</strong></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="title">Tipo de segurança</td>
                                <td>
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>
Sistema baseado em Pathname (caminho do arquivo) e não requer "Etiquetas" ou "Reetiquetamento" do sistema de arquivos.</li>
                                        <li>
Quando desenvolvendo perfis (Profiles) de forma incremental, há muito menos razões para modificar outros perfis, porque todos os profiles simplesmente referem se ao caminho usado</li>
                                        <li>
"Caminhos de Arquivos" (Pathnames) são fáceis de entender e auditar.</li>
                                    </ul>
                                </td>
                                <td>
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>
Anexa etiquetas a todos os arquivos e processos</li>
                                        <li>
Etiquetas identificam os canais de comunicação, para adicionar novos perfis (profiles) pode requerer a alteração de perfis existentes para dividir canais de comunicação, tornando o desenvolvimento de politicas difícil</li>
                                        <li>
Nem todas as aplicações preservam as etiquetas</li>
                                    </ul>
                                </td>
                            </tr>
                            <tr>
                                <td class="title">
Consequências</td>
                                <td>
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>
Ferramentas automatizada</li>
                                        <li>
Fácil integração na plataforma Novel</li>
                                    </ul>
                                </td>
                                <td>
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>
Manutenção Difícil</li>
                                        <li>
Baixa taxa de adoção</li>
                                    </ul>
                                </td>
                            </tr>
                            <tr>
                                <td class="title">
Fácil de usar</td>
                                <td>
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>
Politicas auditáveis</li>
                                        <li>
GUI Integrada, conjunto de ferramentas de console</li>
                                        <li>
Proficiencia com 1 a 2 dias de treino.</li>
                                        <li>
A usabilidade é o objetivo primário</li>
                                    </ul>
                                </td>
                                <td>
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>
Linguagem de definição das politicas complexa</li>
                                        <li>
Regras de difícil gerencia</li>
                                        <li>
Uma lacuna de ferramentas integradas</li>
                                        <li>
Investimento considerável para treinamento</li>
                                    </ul>
                                </td>
                            </tr>
</tbody>
</table>
<figcaption>Tabela comparativa das principais diferenças das estruturas.
</figcaption>
</figure>

### Automação
Conforme também [suse-selinux-comparison] a automação para criação de profiles é bem mais simples e rápida veja a tabela adaptada:

<figure>
<table class="table_comparison table_text">
	<thead>
		<tr>
			<th class="null">&nbsp;</th>
                                <th><strong>AppArmor</strong></th>
                                <th class="last-child"><strong>SELinux</strong></th>
                            </tr>
                        </thead>
<tbody>
                        	<tr>
                        		<td class="title">&nbsp;</td>
                                <td style="vertical-align:top;">
                                    <ol style="padding-left:30px;margin-left:0px;">
                                        <li>Open YaST Control Center</li>
                                        <li>Run Server Analyzer to determine which programs to profile</li>
                                        <li>Run the Profile Wizard to generate a profile template</li>
                                        <li>Run the application through normal operation</li>
                                        <li>Run the interactive optimizer to synthesize log events into a profile</li>
                                    </ol>
                                </td>
                               <td style="vertical-align:top;"><p>SELinux audit2allow</p>			
                                    <ol style="padding-left:30px;margin-left:0px;">
                                        <li>Create a file at $SELINUX_SRC/domains/program/foo.te</li>
                                        <li>Put the daemon domain macro call in the file</li>
                                        <li>Create the file contexts file</li>
                                        <li>Put the first list of file contexts in file.fc</li>
                                        <li>Load the new policy with make load</li>
                                        <li>Label the foo files</li>
                                        <li>Start the daemon, service foo start</li>
                                        <li>Examine your audit log for denial messages</li>
                                        <li>Familiarize yourself with the errors the daemon is generating</li>
                                        <li>Use audit2allow to start the first round of policy rules</li>
                                        <li>Look to see if the foo_t domain tries to create a network socket</li>
                                        <li>Continue to iterate through the basic steps to generate all the rules you need</li>
                                        <li>If the domain tries to access port_t, which relates to tclass=tcp_socket or tclass=udp_socket in the AVC log message, you need to determine what port number foo_t needs to use</li>
                                        <li>Iterate through the remaining AVC denials. When they are resolved with new policy, you can configure the unique port requirements for the foo_t domain</li>
                                        <li>With the daemon started, determine which port foo is using</li>
                                        <li>Remove the generic port_t rule, replacing it with a specific rule for a new port type based on the foo_t domain</li>
                                    </ol>
                                </td>
                            </tr>
                            
                            
                            <tr>
                                <td class="title">&nbsp;</td>
                                <td style="vertical-align:top;">
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>Easy to Use—pre-defined abstractions</li>
                                        <li>Easy to Modify—regular expression &amp; wildcard support</li>
                                        <li>Easy to Audit—classic Unix syntax</li>
                                    </ul>
                                </td>
                                <td style="vertical-align:top;">
                                    <ul style="padding-left:30px;margin-left:0px;">
    
                                        <li>Custom and complex programming language</li>
                                        <li>Hard-to-manage rules</li>
                                    </ul>
                                </td>
                            </tr>
                        </tbody>
                    </table>
<figcaption>Tabela comparativa do processo automatizado.
</figcaption>
</figure>

#### Eficiência

O Código de descrição dos perfis no AppArmor parecem ser mais eficiente, veja a tabela abaixo adaptada de [suse-selinux-compararison]:

<figure>
<table class="table_comparison table_text">
                        <thead>
                            <tr>
                                <th class="null">&nbsp;</th>
                                <th><strong>AppArmor</strong></th>
                                <th class="last-child"><strong>SELinux</strong></th>
                            </tr>
                        </thead>
	<tbody>
		 
		<tr>
			<td class="title">&nbsp;</td>
                                <td style="vertical-align:top;padding-left:15px;margin-left:0px;"><p>usr/sbin/in.ftpd {<br>
                                    #include &lt;immunix-standard/base&gt; <br>
                                    #include &lt;immunix-standard/nameservice&gt; <br>
                                    #include &lt;immunix-standard/authentication&gt; <br>
                                    #include &lt;user-custom/ftpd&gt; <br>
                                    /&nbsp;&nbsp; r,<br>
                                    /dev/urandom                    &nbsp;&nbsp;  r,<br>
                                    /etc/fstab                       &nbsp;&nbsp; r,<br>
                                    /etc/ftpaccess                   &nbsp;&nbsp; r,<br>
                                    /etc/ftpconversions              &nbsp;&nbsp; r,<br>
                                    /etc/ftphosts                     &nbsp;&nbsp;r,<br>
                                    /etc/ftpusers                    &nbsp;&nbsp; r,<br>
                                    /etc/shells                      &nbsp;&nbsp; r,<br>
                                    /usr/sbin/in.ftpd                &nbsp;&nbsp; r,<br>
                                    /usr/share/ssl/certs/ca-bundle.crt        &nbsp;&nbsp;r,<br>
                                    /usr/share/ssl/certs/ftpd-rsa.pem         &nbsp;&nbsp;r,<br>
                                    /usr/share/ssl/private/ftpd-rsa-key.pem   &nbsp;&nbsp;r,<br>
                                    /usr/share/ssl/.rnd             &nbsp;&nbsp;  w,<br>
                                    /var/log/xferlog                 &nbsp;&nbsp; w,<br>
                                    /var/run                          &nbsp;&nbsp;wr,<br>
                                    /var/run/ftp.{pids,rips}-all      &nbsp;&nbsp;wr,<br>
                                    }<br></p>
        
                                    <p><strong>AppArmor profile for the same program is about 4x smaller</strong></p>
                                </td>
                                <td style="vertical-align:top;padding-left:15px;margin-left:0px;"><p>#################################<br>
                                    #<br>
                                    # Rules for the ftpd_t domain <br>
                                    #<br>
                                    type ftp_port_t, port_type;<br>
                                    type ftp_data_port_t, port_type;<br>
                                    daemon_domain(ftpd, `, auth_chkpwd')<br>
                                    type etc_ftpd_t, file_type, sysadmfile;<br><br>
        
                                    can_network(ftpd_t)<br>
                                    can_ypbind(ftpd_t)<br>
                                    allow ftpd_t self:unix_dgram_socket create_socket_perms;<br>
                                    allow ftpd_t self:unix_stream_socket create_socket_perms;<br>
                                    allow ftpd_t self:process {getcap setcap};<br>
                                    allow ftpd_t self:fifo_file rw_file_perms;<br><br>
        
                                    allow ftpd_t bin_t:dir search;<br>
                                    can_exec(ftpd_t, bin_t)<br>
                                    allow ftpd_t { sysctl_t sysctl_kernel_t }:dir search;<br>
                                    allow ftpd_t sysctl_kernel_t:file { getattr read };<br>
                                    allow ftpd_t urandom_device_t:chr_file { getattr read };<br><br>
        
                                    ifdef(`crond.te', `<br>
                                    system_crond_entry(ftpd_exec_t, ftpd_t)<br>
                                    can_exec(ftpd_t, { sbin_t shell_exec_t })<br>
                                    ')<br><br>
        
                                    allow ftpd_t ftp_data_port_t:tcp_socket name_bind;<br><br>
        
                                    ifdef(`ftpd_daemon', `<br>
                                    define(`ftpd_is_daemon', `')<br>
                                    ') dnl end ftpd_daemon<br>
                                    ifdef(`ftpd_is_daemon', `<br>
                                    rw_dir_create_file(ftpd_t, var_lock_t)<br>
                                    allow ftpd_t ftp_port_t:tcp_socket name_bind;<br>
                                    allow ftpd_t self:unix_dgram_socket { sendto };<br>
                                    can_tcp_connect(userdomain, ftpd_t)<br>
                                    ', `<br>
                                    ifdef(`inetd.te', `<br>
                                    domain_auto_trans(inetd_t, ftpd_exec_t, ftpd_t)<br>
                                    ifdef(`tcpd.te', `domain_auto_trans(tcpd_t, ftpd_exec_t, ftpd_t)')<br><br>
        
                                    # Use sockets inherited from inetd.<br>
                                    allow ftpd_t inetd_t:fd use;<br>
                                    allow ftpd_t inetd_t:tcp_socket rw_stream_socket_perms;<br><br>
        
                                    # Send SIGCHLD to inetd on death.<br>
                                    allow ftpd_t inetd_t:process sigchld;<br>
                                    ') dnl end inetd.te<br>
                                    ')dnl end (else) ftp_is_daemon<br>
                                    ifdef(`ftp_shm', `<br>
                                    allow ftpd_t tmpfs_t:file { read write };<br>
                                    allow ftpd_t { tmpfs_t initrc_t }:shm { read write unix_read unix_write associate };<br>
                                    ')<br><br>
        
                                    # Use capabilities.<br>
                                    allow ftpd_t ftpd_t:capability { net_bind_service setuid setgid fowner fsetid chown sys_resource sys_chroot };<br><br>
        
                                    # Append to /var/log/wtmp.<br>
                                    allow ftpd_t wtmp_t:file { getattr append };<br><br>
        
                                    # allow access to /home<br>
                                    allow ftpd_t home_root_t:dir { getattr search };v<br>
        
                                    # Create and modify /var/log/xferlog.<br>
                                    type xferlog_t, file_type, sysadmfile, logfile;<br>
                                    file_type_auto_trans(ftpd_t, var_log_t, xferlog_t, file)<br>
                                    # Execute /bin/ls (can comment this out for proftpd)<br>
                                    # also may need rules to allow tar etc...<br>
                                    can_exec(ftpd_t, ls_exec_t)<br><br>
        
                                    allow { ftpd_t initrc_t } etc_ftpd_t:file r_file_perms;<br>
                                    allow ftpd_t { etc_t resolv_conf_t etc_runtime_t }:file { getattr read };<br>
                                    allow ftpd_t proc_t:file { getattr read };<br><br>
        
        
                                    ')dnl end if ftp_home_dir</p>
                                </td>
                            </tr>
</tbody>
</table>
<figcaption>Tabela comparativa da eficiência em representar as regras.
</figcaption>
</figure>


### Auditória

O código dos profiles também conforme [suse-selinux-comparision] se apresenta mais legível de fácil auditória:
<figure>
<table class="table_comparison table_text">
                        <thead>
                            <tr>
                                <th class="null">&nbsp;</th>
                                <th><strong>AppArmor</strong></th>
                                <th class="last-child"><strong>SELinux</strong></th>
                            </tr>
                        </thead>
	<tbody>
		<tr>
                                <td class="title">&nbsp;</td>
                                <td style="vertical-align:top;padding-left:15px;margin-left:0px;"><p>/usr/sbin/in.ftpd {<br>
                                      #include &lt;immunix-standard/base&gt;<br>
                                      #include &lt;immunix-standard/nameservice&gt;<br>
                                      #include &lt;immunix-standard/authentication&gt;<br>
                                      #include &lt;user-custom/ftpd&gt;<br>
                                      /                             &nbsp;&nbsp;    r,<br>
                                      /dev/urandom                     &nbsp;&nbsp;  r,<br>
                                      /etc/fstab                       &nbsp;&nbsp;  r,<br>
                                      /etc/ftpaccess                    &nbsp;&nbsp; r,<br>
                                      /etc/ftpconversions               &nbsp;&nbsp; r,<br>
                                      /etc/ftphosts                     &nbsp;&nbsp; r,<br>
                                      /etc/ftpusers                     &nbsp;&nbsp; r,<br>
                                      /etc/shells                       &nbsp;&nbsp; r,<br>
                                      /usr/sbin/in.ftpd                 &nbsp;&nbsp; r,<br>
                                      /usr/share/ssl/certs/ca-bundle.crt      &nbsp;&nbsp;   r,<br>
                                      /usr/share/ssl/certs/ftpd-rsa.pem       &nbsp;&nbsp;   r,<br>
                                      /usr/share/ssl/private/ftpd-rsa-key.pem  &nbsp;&nbsp;  r,<br>
                                      /usr/share/ssl/.rnd               &nbsp;&nbsp; w,<br>
                                      /var/log/xferlog                  &nbsp;&nbsp; w,<br>
                                      /var/run                         &nbsp;&nbsp;  wr,<br>
                                      /var/run/ftp.{pids,rips}-all     &nbsp;&nbsp;  wr,<br>
                                                }</p></td>
                                <td style="vertical-align:top;padding-left:15px;margin-left:0px;"><p>ifdef(`ftpd_daemon', `<br>
                                    define(`ftpd_is_daemon', `')<br>
                                    ') dnl end ftpd_daemon<br>
                                    ifdef(`ftpd_is_daemon', `<br>
                                    rw_dir_create_file(ftpd_t, var_lock_t)<br>
                                    allow ftpd_t ftp_port_t:tcp_socket name_bind;<br>
                                    allow ftpd_t self:unix_dgram_socket { sendto };<br>
                                    can_tcp_connect(userdomain, ftpd_t)<br>
                                    ', `<br>
                                    ifdef(`inetd.te', `<br>
                                    domain_auto_trans(inetd_t, ftpd_exec_t, ftpd_t)<br>
                                    ifdef(`tcpd.te', `domain_auto_trans(tcpd_t, ftpd_exec_t, ftpd_t)')<br><br>
                                    
                                    # Use sockets inherited from inetd.<br>
                                    allow ftpd_t inetd_t:fd use;<br>
                                    allow ftpd_t inetd_t:tcp_socket rw_stream_socket_perms;<br><br>
                                    
                                    # Send SIGCHLD to inetd on death.<br>
                                    allow ftpd_t inetd_t:process sigchld;<br>
                                    ') dnl end inetd.te<br>
                                    ')dnl end (else) ftp_is_daemon<br>
                                    ifdef(`ftp_shm', `<br>
                                    allow ftpd_t tmpfs_t:file { read write };</p>
                                </td>
                            </tr>
</tbody>
</table>
<figcaption>Tabela Comparativa da facilidade de auditória do código
</figcaption>
</figure>

### Arquitetura do SELinux vs AppArmor

<figure>
<center>
<img alt="Arquitetura do SELinux" src="/images/linuxmacwindows/SELinux-Architecture.gif" />
<figcaption>**Arquiteura do SELinux - Figura 1**  
*Fonte:  [IBM-Part1-SELinux]
</center>
</figcaption>
</figure>


<figure>
<center>
<img src="/images/linuxmacwindows/AppArmor-Architecture.png" alt="Arquitetura do AppArmor" />  
 <figcaption>**Arquitetura do AppArmor - Figura 2**  
*Fonte: [Linuxformat-AppArmor]*
</center>
</figcaption>
</figure>
## Conclusão (Resumo do Estudo com Abertura para Possíveis novos Trabalhos)

Sem dúvida alguma ambas as ferramentas atingem seus objetivos, e são as melhores escolhas, a SElinux com a chancela da NSA propõem um modelo aparentemente mais robusto desenvolvido em praticamente 10 anos depesquisas, já o modelo AppArmor apresenta uma maior facilidade de uso, atendendo as necessidades do usuário menos especialista, sem deixar de lado a segurança necessária.

É importante aprofundar mais na arquitetura envolvida nas ferramentas, e além disso discutir outras existentes no mercado que tem propostas diferenciadas. Ficando aberto a oportunidade de uma investigação mais profunda, arquitetura, e também mais extensa horizontalmente, outras ferramentas

## Bibliográfica

 - [IBM-dev-mac]  
   https://www.ibm.com/developerworks/community/blogs/752a690f-8e93-4948-b7a3-c060117e8665/entry/b_c3_aa__c3_a1_b_c3_a1_do_mac_no_linux1?lang=en  
   (Visitado 08/02/2016)

 - [IBM-Part1-SELinux] - IBM - Linux Seguro: Parte 1. SELinux  
   História de seu desenvolvimento, arquitetura e princípios operacionais  
   http://www.ibm.com/developerworks/br/library/l-secure-linux-ru/  
   (Visitado em 08/02/2016)
  
 - [IBM-Anatomia-SELinux] - Anatomia do Security-Enhanced Linux (SELinux)  
   http://www.ibm.com/developerworks/br/library/l-selinux/  
   (Visitado em 08/02/2016)

 - [WorldLibrary-AppArmor] - World Library - AppArmor  
  http://www.worldlibrary.org/Article.aspx?ArticleId=0003721191&Title=AppArmor  
   (Visitado 09/02/2016)
	  
 - [NSA-SELinux]  
   https://www.nsa.gov/research/selinux/   
   (Visitado 09/02/2016)

 - [NSA-SELinux-Precursors] - SELinux Precursors in NSA, Research department site
   https://www.nsa.gov/research/_files/selinux/papers/x/text5.shtml  
   (Visitado 09/02/2016)

 - [suse-selinux-comparison] -  
   https://www.suse.com/support/security/apparmor/features/selinux_comparison.html  
   (Visitado 09/02/2016)

 - [MITRE] MITRE Corporation  
   http://www.mitre.org/  
   (Visitado 09/02/2016)

 - [NCSA-TSRG] - NSA Trusted Systems Research Group  
   https://www.nsa.gov/research/ia_research/index.shtml  
   (Visitado 09/02/2016)

 - [Usenix-SubDomain]
   http://usenix.org/legacy/publications/library/proceedings/lisa2000/full_papers/cowan/cowan_html/index.html  
   (Visitado 09/02/2016)

 - [Linuxformat-AppArmor] - Linux Format - AppArmor  
   http://wiki.linuxformat.ru/wiki/LXF83:AppArmor  
   (Visitado 09/02/2016)
