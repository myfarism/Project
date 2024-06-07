import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;


public class List_Laptop extends javax.swing.JFrame {
    private static Connection koneksi;
    private static Statement st;
    private static ResultSet rs;
    public List_Laptop() {
        initComponents();
        try {
            koneksi = Koneksi.getKoneksi();
            st=koneksi.createStatement();
            String query = "select * from list_laptop";
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
        jScrollPane1 = new javax.swing.JScrollPane();
        tblLaptop = new javax.swing.JTable();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        txtKodeLaptop = new javax.swing.JTextField();
        jLabel5 = new javax.swing.JLabel();
        txtJenisLaptop = new javax.swing.JTextField();
        jLabel6 = new javax.swing.JLabel();
        txtHargaSewa = new javax.swing.JTextField();
        btnTambahLaptop = new javax.swing.JButton();
        jButton1 = new javax.swing.JButton();
        jSeparator1 = new javax.swing.JSeparator();
        jLabel2 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        cbKodeLaptop = new javax.swing.JComboBox<>();
        btnHapusLaptop = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setMinimumSize(null);
        addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentShown(java.awt.event.ComponentEvent evt) {
                formComponentShown(evt);
            }
        });

        jLabel1.setFont(new java.awt.Font("Segoe UI", 1, 20)); // NOI18N
        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Assets/Icon Komputer.png"))); // NOI18N
        jLabel1.setText("List Laptop");

        tblLaptop.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {

            },
            new String [] {
                "Kode Laptop", "Jenis Laptop", "Harga Sewa/jam"
            }
        ) {
            boolean[] canEdit = new boolean [] {
                false, false, false
            };

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        jScrollPane1.setViewportView(tblLaptop);

        jLabel3.setFont(new java.awt.Font("Segoe UI", 1, 20)); // NOI18N
        jLabel3.setText("Tambah Laptop");

        jLabel4.setText("Kode Laptop: ");

        txtKodeLaptop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtKodeLaptopActionPerformed(evt);
            }
        });

        jLabel5.setText("Jenis Laptop:");

        txtJenisLaptop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtJenisLaptopActionPerformed(evt);
            }
        });

        jLabel6.setText("Harga Sewa/jam:");

        txtHargaSewa.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                txtHargaSewaActionPerformed(evt);
            }
        });

        btnTambahLaptop.setText("Tambah ");
        btnTambahLaptop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnTambahLaptopActionPerformed(evt);
            }
        });

        jButton1.setText("<");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jLabel2.setFont(new java.awt.Font("Segoe UI", 1, 20)); // NOI18N
        jLabel2.setText("Hapus Laptop");

        jLabel7.setText("Kode Laptop:");

        cbKodeLaptop.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "--Pilih Kode Laptop--" }));
        cbKodeLaptop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cbKodeLaptopActionPerformed(evt);
            }
        });

        btnHapusLaptop.setText("Hapus");
        btnHapusLaptop.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnHapusLaptopActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jSeparator1)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 518, Short.MAX_VALUE)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel3)
                                    .addComponent(jLabel1)
                                    .addComponent(jButton1))
                                .addGap(0, 0, Short.MAX_VALUE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                            .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                                .addComponent(jLabel7)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                                .addComponent(cbKodeLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                                            .addComponent(jLabel2, javax.swing.GroupLayout.Alignment.LEADING))
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(btnHapusLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE))
                                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                            .addGroup(layout.createSequentialGroup()
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addComponent(jLabel4)
                                                    .addComponent(jLabel5))
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addComponent(txtJenisLaptop, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 247, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                    .addComponent(txtKodeLaptop, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 247, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                            .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                                .addComponent(jLabel6)
                                                .addGap(18, 18, 18)
                                                .addComponent(txtHargaSewa, javax.swing.GroupLayout.PREFERRED_SIZE, 247, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                        .addComponent(btnTambahLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, 120, javax.swing.GroupLayout.PREFERRED_SIZE)))
                                .addGap(11, 11, 11)))))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jButton1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jSeparator1, javax.swing.GroupLayout.PREFERRED_SIZE, 10, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 48, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 177, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(12, 12, 12)
                .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                        .addComponent(jLabel4)
                        .addComponent(txtKodeLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(38, 38, 38)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(txtJenisLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel5))))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(txtHargaSewa, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnTambahLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addComponent(jLabel2)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel7)
                    .addComponent(cbKodeLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnHapusLaptop, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void txtKodeLaptopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtKodeLaptopActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtKodeLaptopActionPerformed

    private void txtJenisLaptopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtJenisLaptopActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtJenisLaptopActionPerformed

    private void txtHargaSewaActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_txtHargaSewaActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_txtHargaSewaActionPerformed

    private void formComponentShown(java.awt.event.ComponentEvent evt) {//GEN-FIRST:event_formComponentShown
        // TODO add your handling code here:
        DefaultTableModel tbl = (DefaultTableModel) tblLaptop.getModel();
        tbl.setNumRows(0);
        try {
            while (rs.next()){
                cbKodeLaptop.addItem(rs.getString("kode_laptop"));
                tbl.addRow(new Object[]{
                rs.getString("kode_laptop"),
                rs.getString("jenis_laptop"),
                rs.getString("harga_sewa")
            });
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Data Error" + e.getMessage());
        }
    }//GEN-LAST:event_formComponentShown

    private void btnTambahLaptopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnTambahLaptopActionPerformed
        // TODO add your handling code here:
        String txtKodeLaptopString = txtKodeLaptop.getText();
        String txtJenisLaptopString = txtJenisLaptop.getText();
        String txtHargaSewaString = txtHargaSewa.getText();
        
        String query = "insert into list_laptop(kode_laptop, jenis_laptop, harga_sewa) values('"
                +txtKodeLaptopString+"', '"
                +txtJenisLaptopString+"', '"
                +txtHargaSewaString+"')";
        try {
            st.executeUpdate(query);
            JOptionPane.showMessageDialog(this, "Data Laptop Berhasil ditambah");
            txtKodeLaptop.setText("");
            txtJenisLaptop.setText("");
            txtHargaSewa.setText("");
            
            String newLaptop = txtKodeLaptopString;
            cbKodeLaptop.addItem(newLaptop);
            
            rs = st.executeQuery("select * from list_laptop;");
            DefaultTableModel tbl = (DefaultTableModel) tblLaptop.getModel();
            tbl.setNumRows(0);
            while (rs.next()) {
                tbl.addRow(new Object[]{
                    rs.getString("kode_laptop"),
                    rs.getString("jenis_laptop"),
                    rs.getString("harga_sewa")
                });
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this,"Penambahan Data Gagal " +e.getMessage());
        }
    }//GEN-LAST:event_btnTambahLaptopActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        // TODO add your handling code here:
        this.dispose();
    }//GEN-LAST:event_jButton1ActionPerformed

    private void cbKodeLaptopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cbKodeLaptopActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_cbKodeLaptopActionPerformed

    private void btnHapusLaptopActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnHapusLaptopActionPerformed
        // TODO add your handling code here:
        String a = (String) cbKodeLaptop.getSelectedItem();

        if (a.equals("--Pilih Kode Laptop--")) {
            JOptionPane.showMessageDialog(this, "Silakan pilih Kode Laptop yang akan dihapus");
            return;
        }

        int confirm = JOptionPane.showConfirmDialog(this, "Apakah Anda yakin ingin menghapus data laptop dengan Kode Laptop: " + a + "?", "Konfirmasi Hapus", JOptionPane.YES_NO_OPTION);

        if (confirm == JOptionPane.YES_OPTION) {
            String deleteQuery = "DELETE FROM list_laptop WHERE kode_laptop = '" + a + "'";
            try {
                st.executeUpdate(deleteQuery);
                JOptionPane.showMessageDialog(this, "Data Laptop Berhasil dihapus");
                rs = st.executeQuery("SELECT * FROM list_laptop;");
                DefaultTableModel tbl = (DefaultTableModel) tblLaptop.getModel();
                tbl.setNumRows(0);
                cbKodeLaptop.removeAllItems();
                cbKodeLaptop.addItem("--Pilih Kode Laptop--");
                while (rs.next()) {
                    cbKodeLaptop.addItem(rs.getString("kode_laptop"));
                    tbl.addRow(new Object[]{
                        rs.getString("kode_laptop"),
                        rs.getString("jenis_laptop"),
                        rs.getString("harga_sewa")
                    });
                }
            } catch (Exception e) {
                JOptionPane.showMessageDialog(this, "Penghapusan Data Gagal " + e.getMessage());
            }
        }
    }//GEN-LAST:event_btnHapusLaptopActionPerformed

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
            java.util.logging.Logger.getLogger(List_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(List_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(List_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(List_Laptop.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new List_Laptop().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnHapusLaptop;
    private javax.swing.JButton btnTambahLaptop;
    private javax.swing.JComboBox<String> cbKodeLaptop;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JTable tblLaptop;
    private javax.swing.JTextField txtHargaSewa;
    private javax.swing.JTextField txtJenisLaptop;
    private javax.swing.JTextField txtKodeLaptop;
    // End of variables declaration//GEN-END:variables
}