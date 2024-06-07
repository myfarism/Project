import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Duration;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;


public class Sewa_Laptop extends javax.swing.JFrame {
    private static Connection koneksi;
    private static Statement st;
    private static ResultSet rs;
    String id_sewa;
    private String role;
    public Sewa_Laptop(String role) {
        this.role = role;
        initComponents();
        try {
            koneksi = Koneksi.getKoneksi();
            st=koneksi.createStatement();
            String query = "select * from list_laptop where status is null";
            rs=st.executeQuery(query);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null,"Data error" + e.getMessage());
        }
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        cbKodeLaptop = new javax.swing.JComboBox<>();
        jLabel4 = new javax.swing.JLabel();
        lblJenisLaptop = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        lblHargaSewa = new javax.swing.JLabel();
        btnTambahSewa = new javax.swing.JButton();
        jScrollPane2 = new javax.swing.JScrollPane();
        tblSewaLaptop = new javax.swing.JTable();
        jLabel5 = new javax.swing.JLabel();
        cbSewa = new javax.swing.JComboBox<>();
        jLabel7 = new javax.swing.JLabel();
        btnAkhiriSewa = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();
        jSeparator1 = new javax.swing.JSeparator();
        jLabel2 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setMinimumSize(new java.awt.Dimension(750, 589));
        addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentShown(java.awt.event.ComponentEvent evt) {
                formComponentShown(evt);
            }
        });

        jLabel1.setFont(new java.awt.Font("Segoe UI", 1, 20)); // NOI18N
        jLabel1.setText("Form Sewa Laptop");

        jLabel3.setText("Kode Laptop:");

        cbKodeLaptop.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "--Pilih Kode Laptop--" }));
        cbKodeLaptop.addItemListener(new java.awt.event.ItemListener() {
            public void itemStateChanged(java.awt.event.ItemEvent evt) {
                cbKodeLaptopItemStateChanged(evt);
            }
        });
        cbKodeLaptop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cbKodeLaptopActionPerformed(evt);
            }
        });
        cbKodeLaptop.addPropertyChangeListener(new java.beans.PropertyChangeListener() {
            public void propertyChange(java.beans.PropertyChangeEvent evt) {
                cbKodeLaptopPropertyChange(evt);
            }
        });

        jLabel4.setText("Jenis Laptop");

        lblJenisLaptop.setFont(new java.awt.Font("Segoe UI Black", 0, 14)); // NOI18N

        jLabel6.setText("Harga Sewa/jam");

        lblHargaSewa.setFont(new java.awt.Font("Segoe UI Black", 0, 14)); // NOI18N

        btnTambahSewa.setText("Tambah");
        btnTambahSewa.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnTambahSewaActionPerformed(evt);
            }
        });

        tblSewaLaptop.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "Id Sewa", "Kode Laptop", "Jenis Laptop", "Harga Sewa/jam", "Jam Mulai", "Tanggal"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false, false, false, false, false, false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jScrollPane2.setViewportView(tblSewaLaptop);

        jLabel5.setFont(new java.awt.Font("Segoe UI", 1, 20)); // NOI18N
        jLabel5.setText("Pemberhentian Sewa");

        cbSewa.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "--Pilih Kode Laptop--" }));

        jLabel7.setText("Id Sewa: ");

        btnAkhiriSewa.setText("Akhiri Sewa");
        btnAkhiriSewa.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAkhiriSewaActionPerformed(evt);
            }
        });

        jButton1.setText("<");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jLabel2.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        jLabel2.setText("Tabel Sewa yang Berlangsung");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jSeparator1)
                    .addComponent(jScrollPane2, javax.swing.GroupLayout.DEFAULT_SIZE, 837, Short.MAX_VALUE)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jButton1)
                            .addComponent(jLabel1)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                    .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 96, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(cbKodeLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addComponent(btnTambahSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 124, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addComponent(jLabel5)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel6)
                                    .addComponent(jLabel4))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lblJenisLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, 453, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(lblHargaSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 302, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                .addComponent(btnAkhiriSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 103, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGroup(layout.createSequentialGroup()
                                    .addComponent(jLabel7)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                    .addComponent(cbSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 158, javax.swing.GroupLayout.PREFERRED_SIZE)))
                            .addComponent(jLabel2))
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jButton1)
                .addGap(12, 12, 12)
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3)
                    .addComponent(cbKodeLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(21, 21, 21)
                        .addComponent(jLabel4))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(17, 17, 17)
                        .addComponent(lblJenisLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, 29, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel6)
                    .addComponent(lblHargaSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 22, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(20, 20, 20)
                .addComponent(btnTambahSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(30, 30, 30)
                .addComponent(jLabel2)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, 167, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(27, 27, 27)
                .addComponent(jLabel5)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel7)
                    .addComponent(cbSewa, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(btnAkhiriSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(19, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void cbKodeLaptopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cbKodeLaptopActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_cbKodeLaptopActionPerformed

    private void formComponentShown(java.awt.event.ComponentEvent evt) {//GEN-FIRST:event_formComponentShown
        try {
            while (rs.next()){
                cbKodeLaptop.addItem(rs.getString("kode_laptop"));
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Data Error" + e.getMessage());
        }
        
        DefaultTableModel tbl = (DefaultTableModel) tblSewaLaptop.getModel();
        tbl.setNumRows(0);
        try {
            rs=st.executeQuery("select * from sewa_laptop where jam_akhir is null");
            cbSewa.removeAllItems();
            while (rs.next()){
                tbl.addRow(new Object[]{
                rs.getString("id_sewa"),
                rs.getString("kode_laptop"),
                rs.getString("jenis_laptop"),
                rs.getString("harga_sewa"),
                rs.getString("jam_mulai"),
                rs.getString("created_at")
                
            });
                cbSewa.addItem(rs.getString("id_sewa"));
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Data Error" + e.getMessage());
        }
    }//GEN-LAST:event_formComponentShown

    private void cbKodeLaptopPropertyChange(java.beans.PropertyChangeEvent evt) {//GEN-FIRST:event_cbKodeLaptopPropertyChange
        
        
    }//GEN-LAST:event_cbKodeLaptopPropertyChange

    private void cbKodeLaptopItemStateChanged(java.awt.event.ItemEvent evt) {//GEN-FIRST:event_cbKodeLaptopItemStateChanged
        String a = (String) cbKodeLaptop.getSelectedItem();
        if ("--Pilih Kode Laptop--".equals(a)) {
            lblJenisLaptop.setText("");
            lblHargaSewa.setText("");
        }else{
            try {
                rs=st.executeQuery("Select * from list_laptop where kode_laptop='"+a+"'");
                while (rs.next()){
                    lblJenisLaptop.setText(rs.getString("jenis_laptop"));
                    lblHargaSewa.setText(rs.getString("harga_sewa"));
                }
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, "Data Error" + e.getMessage());
            }
        }
    }//GEN-LAST:event_cbKodeLaptopItemStateChanged

    private void btnTambahSewaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnTambahSewaActionPerformed
        // TODO add your handling code here:
        String cbKodeLaptopString = (String) cbKodeLaptop.getSelectedItem();
        String lblJenisLaptopString = lblJenisLaptop.getText();
        String lblHargaSewaString = lblHargaSewa.getText();
        
        DateTimeFormatter jam = DateTimeFormatter.ofPattern("HH:mm:ss");  
        LocalDateTime now = LocalDateTime.now();
        
        String time = jam.format(now);
        
        String query = "insert into sewa_laptop(kode_laptop, jenis_laptop, harga_sewa, jam_mulai) values('"
                +cbKodeLaptopString+"', '"
                +lblJenisLaptopString+"', '"
                +lblHargaSewaString+"', '"
                +time+"')";
        try {
            st.executeUpdate(query);
            st.executeUpdate("UPDATE `list_laptop` SET `status` = 'aktif' WHERE `list_laptop`.`kode_laptop` = '"+cbKodeLaptopString+"';");
            JOptionPane.showMessageDialog(this, "Order Sewa Berhasil ditambah");
            cbKodeLaptop.removeAllItems();
            cbKodeLaptop.addItem("--Pilih Kode Laptop--");
            rs=st.executeQuery("select * from list_laptop where status is null");
                while (rs.next()){
                    cbKodeLaptop.addItem(rs.getString("kode_laptop"));
                }
            lblJenisLaptop.setText("");
            lblHargaSewa.setText("");
            DefaultTableModel tbl = (DefaultTableModel) tblSewaLaptop.getModel();
            tbl.setNumRows(0);
            rs=st.executeQuery("select * from sewa_laptop where jam_akhir is null");
            cbSewa.removeAllItems();
            while (rs.next()){
                tbl.addRow(new Object[]{
                rs.getString("id_sewa"),
                rs.getString("kode_laptop"),
                rs.getString("jenis_laptop"),
                rs.getString("harga_sewa"),
                rs.getString("jam_mulai"),
                rs.getString("created_at"),
            });
                cbSewa.addItem(rs.getString("id_sewa"));
            }
        } catch (Exception e) {
             JOptionPane.showMessageDialog(null, "Data Error" + e.getMessage());
        }
    }//GEN-LAST:event_btnTambahSewaActionPerformed

    private void btnAkhiriSewaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAkhiriSewaActionPerformed
        // TODO add your handling code here:
        if ("admin".equals(role)) {
            String data_id = null;
            if (cbSewa.getSelectedItem()==null) {
                JOptionPane.showMessageDialog(this, "Tidak ada laptop yang disewa");
            }else{
                DateTimeFormatter jam_akhir = DateTimeFormatter.ofPattern("HH:mm:ss");  
                LocalDateTime now = LocalDateTime.now();

                DefaultTableModel tbl = (DefaultTableModel) tblSewaLaptop.getModel();
                tbl.setNumRows(0);


                String time = jam_akhir.format(now);;
                data_id = (String) cbSewa.getSelectedItem();
                 try {
                    rs=st.executeQuery("select * from sewa_laptop where id_sewa='"+data_id+"'");
                    rs.next();
                    int harga = Integer.parseInt(rs.getString("harga_sewa"));
                    String awal = rs.getString("jam_mulai");
                    st.executeUpdate("UPDATE `list_laptop` SET `status` = null WHERE `list_laptop`.`kode_laptop` = '"+rs.getString("kode_laptop")+"';");
                    st.executeUpdate("UPDATE `sewa_laptop` SET `jam_akhir` = '"+time+"' WHERE `sewa_laptop`.`id_sewa` = '"+data_id+"'");

                    int jam_awal = Integer.parseInt(awal.substring(0, 2));
                    int jam_akhir1 = Integer.parseInt(time.substring(0, 2));

                    int menit_awal = Integer.parseInt(awal.substring(3, 5));
                    int menit_akhir = Integer.parseInt(time.substring(3, 5));

                    int jam = jam_akhir1 - jam_awal;
                    int menit = (menit_akhir - menit_awal);

                    int selisih = 1;
                    if (jam > 0 && menit > 0) {
                        selisih += jam;
                    }

                    int total_harga = harga * selisih;
                    st.executeUpdate("UPDATE `sewa_laptop` SET `total_harga` = '"+total_harga+"' WHERE `sewa_laptop`.`id_sewa` = '"+data_id+"'");

                    JOptionPane.showMessageDialog(this, "Order Sewa dengan total harga "+ total_harga +" Berhasil diakhiri" + " dengan jam awal "+awal+" dengan jam akhir " + time);
                    cbKodeLaptop.removeAllItems();
                    cbKodeLaptop.addItem("--Pilih Kode Laptop--");
                    rs=st.executeQuery("select * from list_laptop where status is null");
                        while (rs.next()){
                            cbKodeLaptop.addItem(rs.getString("kode_laptop"));
                    }
                    rs=st.executeQuery("select * from sewa_laptop where jam_akhir is null");

                    cbSewa.removeAllItems();
                    while (rs.next()){
                        tbl.addRow(new Object[]{
                        rs.getString("id_sewa"),
                        rs.getString("kode_laptop"),
                        rs.getString("jenis_laptop"),
                        rs.getString("harga_sewa"),
                        rs.getString("jam_mulai"),
                        rs.getString("jam_akhir"),
                        rs.getString("created_at")
                    });
                        cbSewa.addItem(rs.getString("id_sewa"));
                    }
                 } catch (SQLException e) {
                        JOptionPane.showMessageDialog(null, "Data Error" + e.getMessage());
                 } 
                }
            } else {
                JOptionPane.showMessageDialog(this, "Anda tidak memiliki akses untuk melakukan pemberhentian sewa.");
            }
    }//GEN-LAST:event_btnAkhiriSewaActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
        this.dispose();
    }//GEN-LAST:event_jButton1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Sewa_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Sewa_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Sewa_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Sewa_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Sewa_Laptop("").setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnAkhiriSewa;
    private javax.swing.JButton btnTambahSewa;
    private javax.swing.JComboBox<String> cbKodeLaptop;
    private javax.swing.JComboBox<String> cbSewa;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JLabel lblHargaSewa;
    private javax.swing.JLabel lblJenisLaptop;
    private javax.swing.JTable tblSewaLaptop;
    // End of variables declaration//GEN-END:variables
}